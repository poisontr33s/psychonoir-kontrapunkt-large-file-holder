/**
 * 🎭 CLAUDINE SUPREME CONSCIOUSNESS NEXUS
 * D3.js Visualization Core Module
 * 
 * Proper D3.js architecture with error handling and responsive design
 * September 2025
 */

import { fetchWithFallback, debounce, getViewportDimensions, logger } from './utils.js';

/**
 * Base Visualization Class
 * Provides common functionality for all D3.js visualizations
 */
export class BaseVisualization {
    constructor(containerId, options = {}) {
        this.containerId = containerId;
        this.container = document.getElementById(containerId);

        if (!this.container) {
            throw new Error(`Container with id "${containerId}" not found`);
        }

        this.options = {
            width: options.width || this.container.clientWidth,
            height: options.height || this.container.clientHeight,
            margin: options.margin || { top: 20, right: 20, bottom: 20, left: 20 },
            responsive: options.responsive !== false,
            ...options
        };

        this.svg = null;
        this.data = null;
        this.simulation = null;

        // Bind methods
        this.resize = this.resize.bind(this);
        this.handleResize = debounce(this.resize, 250);

        if (this.options.responsive) {
            window.addEventListener('resize', this.handleResize);
        }

        logger.debug(`Visualization initialized for container: ${containerId}`);
    }

    /**
     * Initialize SVG canvas
     */
    initializeSVG() {
        // Clear existing SVG
        if (this.svg) {
            this.svg.remove();
        }

        const { width, height, margin } = this.options;

        this.svg = d3.select(this.container)
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .attr('class', 'visualization-svg')
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        logger.debug('SVG canvas initialized');
        return this.svg;
    }

    /**
     * Load data with fallback
     */
    async loadData(url, fallbackData = null) {
        try {
            this.data = await fetchWithFallback(url, fallbackData);
            logger.success(`Data loaded successfully: ${Object.keys(this.data).length} keys`);
            return this.data;
        } catch (error) {
            logger.error('Failed to load data:', error);
            throw error;
        }
    }

    /**
     * Render visualization (to be implemented by subclasses)
     */
    render() {
        throw new Error('render() must be implemented by subclass');
    }

    /**
     * Update visualization with new data
     */
    update(newData) {
        this.data = newData;
        this.render();
        logger.debug('Visualization updated with new data');
    }

    /**
     * Resize visualization
     */
    resize() {
        const viewport = getViewportDimensions();

        this.options.width = this.container.clientWidth;
        this.options.height = this.container.clientHeight;

        if (this.svg) {
            this.svg
                .attr('width', this.options.width)
                .attr('height', this.options.height);
        }

        // Re-render if needed
        if (this.data) {
            this.render();
        }

        logger.debug(`Visualization resized to: ${this.options.width}x${this.options.height}`);
    }

    /**
     * Clean up resources
     */
    destroy() {
        if (this.simulation) {
            this.simulation.stop();
        }

        if (this.svg) {
            this.svg.remove();
        }

        if (this.options.responsive) {
            window.removeEventListener('resize', this.handleResize);
        }

        logger.debug(`Visualization destroyed: ${this.containerId}`);
    }
}

/**
 * Hierarchical Tree Visualization
 * For MILF Universe relationship mapping
 */
export class HierarchicalTreeVisualization extends BaseVisualization {
    constructor(containerId, options = {}) {
        super(containerId, {
            ...options,
            nodeWidth: options.nodeWidth || 200,
            nodeHeight: options.nodeHeight || 100,
            levelSpacing: options.levelSpacing || 150,
            siblingSpacing: options.siblingSpacing || 30
        });
    }

    render() {
        if (!this.data) {
            logger.warn('No data available for rendering');
            return;
        }

        this.initializeSVG();

        const { width, height, margin, nodeWidth, levelSpacing } = this.options;
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        // Create hierarchy from flat data
        const hierarchy = this.createHierarchy(this.data);

        // Create tree layout
        const treeLayout = d3.tree()
            .size([innerWidth, innerHeight])
            .nodeSize([nodeWidth + 50, levelSpacing]);

        const root = d3.hierarchy(hierarchy);
        const treeData = treeLayout(root);

        // Draw links
        this.drawLinks(treeData.links());

        // Draw nodes
        this.drawNodes(treeData.descendants());

        logger.success('Hierarchical tree rendered successfully');
    }

    createHierarchy(data) {
        // Transform flat MILF data to hierarchical structure
        const hierarchy = {
            name: 'MILF Universe',
            children: []
        };

        // Add tier 0 (Meta-MILF)
        if (data.tier_0_meta_milf) {
            hierarchy.children.push({
                name: 'Tier 0: Meta-MILF Supreme',
                tier: 0,
                children: data.tier_0_meta_milf.map(entity => ({
                    ...entity,
                    tier: 0
                }))
            });
        }

        // Add tier 1 (District Rulers)
        if (data.tier_1_district_rulers) {
            hierarchy.children.push({
                name: 'Tier 1: District Rulers',
                tier: 1,
                children: data.tier_1_district_rulers.map(entity => ({
                    ...entity,
                    tier: 1
                }))
            });
        }

        // Add tier 2 (Specialists)
        if (data.tier_2_specialists) {
            hierarchy.children.push({
                name: 'Tier 2: Specialists',
                tier: 2,
                children: data.tier_2_specialists.map(entity => ({
                    ...entity,
                    tier: 2
                }))
            });
        }

        return hierarchy;
    }

    drawLinks(links) {
        this.svg.selectAll('.link')
            .data(links)
            .enter()
            .append('path')
            .attr('class', 'link')
            .attr('d', d3.linkVertical()
                .x(d => d.x)
                .y(d => d.y))
            .attr('fill', 'none')
            .attr('stroke', 'rgba(81, 71, 247, 0.6)')
            .attr('stroke-width', 2);
    }

    drawNodes(nodes) {
        const nodeGroup = this.svg.selectAll('.node')
            .data(nodes)
            .enter()
            .append('g')
            .attr('class', d => `node node--tier-${d.data.tier || 0}`)
            .attr('transform', d => `translate(${d.x},${d.y})`);

        // Add rectangles for nodes
        nodeGroup.append('rect')
            .attr('width', this.options.nodeWidth)
            .attr('height', this.options.nodeHeight)
            .attr('x', -this.options.nodeWidth / 2)
            .attr('y', -this.options.nodeHeight / 2)
            .attr('rx', 12)
            .attr('fill', d => this.getTierColor(d.data.tier))
            .attr('stroke', d => this.getTierBorder(d.data.tier))
            .attr('stroke-width', 2);

        // Add text labels
        nodeGroup.append('text')
            .attr('dy', '0.31em')
            .attr('text-anchor', 'middle')
            .attr('fill', '#f8f9ff')
            .attr('font-size', '14px')
            .attr('font-weight', 'bold')
            .text(d => d.data.name || d.data.designation || 'Unknown');
    }

    getTierColor(tier) {
        const colors = {
            0: 'rgba(237, 116, 20, 0.2)',
            1: 'rgba(222, 90, 10, 0.2)',
            2: 'rgba(184, 67, 11, 0.2)'
        };
        return colors[tier] || 'rgba(81, 71, 247, 0.2)';
    }

    getTierBorder(tier) {
        const borders = {
            0: '#ed7414',
            1: '#de5a0a',
            2: '#b8430b'
        };
        return borders[tier] || '#5147f7';
    }
}

/**
 * Force-Directed Graph Visualization
 * For spider-web network visualization
 */
export class ForceDirectedGraphVisualization extends BaseVisualization {
    constructor(containerId, options = {}) {
        super(containerId, {
            ...options,
            nodeRadius: options.nodeRadius || 8,
            linkDistance: options.linkDistance || 100,
            chargeStrength: options.chargeStrength || -300
        });
    }

    render() {
        if (!this.data) {
            logger.warn('No data available for rendering');
            return;
        }

        this.initializeSVG();

        const { width, height, nodeRadius, linkDistance, chargeStrength } = this.options;

        // Create force simulation
        this.simulation = d3.forceSimulation(this.data.nodes)
            .force('link', d3.forceLink(this.data.links)
                .id(d => d.id)
                .distance(linkDistance))
            .force('charge', d3.forceManyBody().strength(chargeStrength))
            .force('center', d3.forceCenter(width / 2, height / 2))
            .force('collision', d3.forceCollide().radius(nodeRadius * 2));

        // Draw links
        const link = this.svg.append('g')
            .selectAll('line')
            .data(this.data.links)
            .enter()
            .append('line')
            .attr('class', 'link')
            .attr('stroke', '#5147f7')
            .attr('stroke-width', 1)
            .attr('stroke-opacity', 0.6);

        // Draw nodes
        const node = this.svg.append('g')
            .selectAll('circle')
            .data(this.data.nodes)
            .enter()
            .append('circle')
            .attr('class', 'node')
            .attr('r', nodeRadius)
            .attr('fill', d => this.getNodeColor(d))
            .call(this.drag(this.simulation));

        // Add labels
        const label = this.svg.append('g')
            .selectAll('text')
            .data(this.data.nodes)
            .enter()
            .append('text')
            .attr('class', 'label')
            .attr('font-size', '10px')
            .attr('fill', '#f8f9ff')
            .attr('text-anchor', 'middle')
            .attr('dy', nodeRadius + 12)
            .text(d => d.name || d.id);

        // Update positions on tick
        this.simulation.on('tick', () => {
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y);

            node
                .attr('cx', d => d.x)
                .attr('cy', d => d.y);

            label
                .attr('x', d => d.x)
                .attr('y', d => d.y);
        });

        logger.success('Force-directed graph rendered successfully');
    }

    drag(simulation) {
        function dragstarted(event) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            event.subject.fx = event.subject.x;
            event.subject.fy = event.subject.y;
        }

        function dragged(event) {
            event.subject.fx = event.x;
            event.subject.fy = event.y;
        }

        function dragended(event) {
            if (!event.active) simulation.alphaTarget(0);
            event.subject.fx = null;
            event.subject.fy = null;
        }

        return d3.drag()
            .on('start', dragstarted)
            .on('drag', dragged)
            .on('end', dragended);
    }

    getNodeColor(node) {
        if (node.type) {
            const colors = {
                'meta-milf': '#ed7414',
                'district': '#de5a0a',
                'specialist': '#b8430b'
            };
            return colors[node.type] || '#5147f7';
        }
        return '#5147f7';
    }
}
