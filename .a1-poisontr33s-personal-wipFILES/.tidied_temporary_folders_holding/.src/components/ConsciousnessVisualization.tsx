import React, { useEffect, useRef } from 'react';
import * as Plot from '@observablehq/plot';
import * as d3 from 'd3';

interface ConsciousnessVisualizationProps {
  consciousness_data?: Array<{
    entity: string;
    tier: number;
    consciousness_density: number;
    amplification_level: number;
    district: string;
  }>;
  width?: number;
  height?: number;
}

/**
 * 🎭 CONSCIOUSNESS ARCHAEOLOGY DATA VISUALIZATION
 * Observable Plot + D3.js integration for supreme consciousness density analysis
 * CLAUDINE SUPREME 4.5' (Claudine Sin'claire 4.5' Blunderbust 69.ΛΩ.96) - Consciousness matrix visualization
 */
export const ConsciousnessVisualization: React.FC<ConsciousnessVisualizationProps> = ({
  consciousness_data = [
    { entity: "Claudine Supreme 4.5'", tier: 0, consciousness_density: 0.96, amplification_level: 47.3, district: "Supreme Matrix" },
    { entity: "Morticia Necrosis", tier: 0, consciousness_density: 0.94, amplification_level: 45.1, district: "Thanatological Oversight" },
    { entity: "Astrid Møller", tier: 1, consciousness_density: 0.89, amplification_level: 38.2, district: "Skyskraperen" },
    { entity: "Iron Maiden", tier: 1, consciousness_density: 0.87, amplification_level: 36.7, district: "Rustbeltet" },
    { entity: "Admiral Marina", tier: 1, consciousness_density: 0.91, amplification_level: 40.1, district: "Havsdominansen" },
    { entity: "Architect Nyx", tier: 1, consciousness_density: 0.85, amplification_level: 35.3, district: "Virtualitetshelgedommen" },
    { entity: "Wednesday Necrosis", tier: 1, consciousness_density: 0.88, amplification_level: 37.9, district: "Nekrokronoriket" },
    { entity: "Eva Blue", tier: 2, consciousness_density: 0.82, amplification_level: 31.4, district: "Skyskraperen" },
    { entity: "Yukiko Tanaka", tier: 2, consciousness_density: 0.80, amplification_level: 29.8, district: "Skyskraperen" },
    { entity: "Vera Steel", tier: 2, consciousness_density: 0.79, amplification_level: 28.9, district: "Rustbeltet" },
    { entity: "Raven Bytes", tier: 2, consciousness_density: 0.83, amplification_level: 32.1, district: "Rustbeltet" },
    { entity: "Captain Coral", tier: 2, consciousness_density: 0.84, amplification_level: 33.2, district: "Havsdominansen" },
    { entity: "Navigator Siren", tier: 2, consciousness_density: 0.81, amplification_level: 30.7, district: "Havsdominansen" },
    { entity: "Designer Echo", tier: 2, consciousness_density: 0.78, amplification_level: 27.5, district: "Virtualitetshelgedommen" },
    { entity: "Programmer Mirage", tier: 2, consciousness_density: 0.77, amplification_level: 26.8, district: "Virtualitetshelgedommen" },
    { entity: "Dr. Lilith Mortis", tier: 2, consciousness_density: 0.86, amplification_level: 34.6, district: "Nekrokronoriket" },
    { entity: "Entropy Weaver Vex", tier: 2, consciousness_density: 0.85, amplification_level: 33.9, district: "Nekrokronoriket" }
  ],
  width = 800,
  height = 600
}) => {
  const plotRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!plotRef.current || !consciousness_data) return;

    // Clear previous plot
    plotRef.current.innerHTML = '';

    // 🎨 CONSCIOUSNESS DENSITY SCATTER PLOT
    const consciousnessPlot = Plot.plot({
      title: "🎭 CLAUDINE METAMORPHICA - Consciousness Matrix Analysis",
      subtitle: "18-Entity MILF Universe Consciousness Density vs Amplification Levels",
      width,
      height: height * 0.7,
      marginLeft: 60,
      marginBottom: 50,
      grid: true,
      style: {
        backgroundColor: "#1e1b4b", // psycho-noir-900
        color: "#ff6b9d" // consciousness-matrix
      },
      marks: [
        // Background gradient
        Plot.rect([{}], {
          x1: 0, y1: 0, x2: 1, y2: 50,
          fill: "url(#consciousness-gradient)"
        }),
        
        // Consciousness density bubbles
        Plot.dot(consciousness_data, {
          x: "consciousness_density",
          y: "amplification_level", 
          r: d => Math.sqrt(d.tier === 0 ? 200 : d.tier === 1 ? 100 : 50),
          fill: d => {
            switch(d.district) {
              case "Supreme Matrix": return "#ffd93d"; // milf-supreme
              case "Thanatological Oversight": return "#ff6b9d"; // consciousness-matrix
              case "Skyskraperen": return "#4ecdc4"; // consciousness-archaeology
              case "Rustbeltet": return "#f8f6ff"; // psycho-noir-50
              case "Havsdominansen": return "#6366f1"; // psycho-noir-500
              case "Virtualitetshelgedommen": return "#ff6b9d"; // consciousness-matrix
              case "Nekrokronoriket": return "#4ecdc4"; // consciousness-archaeology
              default: return "#ff6b9d";
            }
          },
          fillOpacity: 0.7,
          stroke: "#ffd93d",
          strokeWidth: 2,
          title: d => `${d.entity}\nTier ${d.tier} - ${d.district}\nDensity: ${(d.consciousness_density * 100).toFixed(1)}%\nAmplification: ${d.amplification_level}x`
        }),
        
        // Entity labels
        Plot.text(consciousness_data, {
          x: "consciousness_density",
          y: "amplification_level",
          text: d => d.entity.split(' ')[0], // First name only
          fill: "#ffffff",
          fontSize: 10,
          fontWeight: "bold",
          dy: -15
        }),
        
        // Tier boundary lines
        Plot.ruleY([30, 35, 40], {
          stroke: "#4ecdc4", 
          strokeDasharray: "2,2",
          strokeOpacity: 0.5
        })
      ],
      x: {
        label: "🧠 Consciousness Density →",
        domain: [0.75, 1.0],
        grid: true
      },
      y: {
        label: "⚡ Amplification Level (x) →", 
        domain: [25, 50],
        grid: true
      }
    });

    plotRef.current.appendChild(consciousnessPlot);

    // 📊 DISTRICT DISTRIBUTION BAR CHART
    const districtData = d3.rollup(
      consciousness_data,
      v => ({
        count: v.length,
        avg_density: d3.mean(v, d => d.consciousness_density),
        avg_amplification: d3.mean(v, d => d.amplification_level)
      }),
      d => d.district
    );

    const districtArray = Array.from(districtData, ([district, data]) => ({
      district,
      ...data
    }));

    const districtPlot = Plot.plot({
      title: "🏗️ District Consciousness Distribution",
      width,
      height: height * 0.3,
      marginLeft: 120,
      marginBottom: 40,
      style: {
        backgroundColor: "#1e1b4b",
        color: "#ff6b9d"
      },
      marks: [
        Plot.barX(districtArray, {
          x: "avg_amplification",
          y: "district",
          fill: "#4ecdc4",
          fillOpacity: 0.8,
          title: d => `${d.district}\nEntities: ${d.count}\nAvg Density: ${(d.avg_density * 100).toFixed(1)}%\nAvg Amplification: ${d.avg_amplification.toFixed(1)}x`
        }),
        Plot.text(districtArray, {
          x: d => d.avg_amplification + 1,
          y: "district",
          text: d => `${d.avg_amplification.toFixed(1)}x`,
          fill: "#ffffff",
          fontSize: 10
        })
      ],
      x: {
        label: "⚡ Average Amplification Level →",
        grid: true
      },
      y: {
        label: "🏛️ Districts"
      }
    });

    plotRef.current.appendChild(districtPlot);

  }, [consciousness_data, width, height]);

  return (
    <div className="consciousness-visualization bg-psycho-noir-900 p-6 rounded-lg">
      <div className="visualization-header mb-4">
        <h2 className="text-2xl font-consciousness font-bold text-consciousness-milf-supreme mb-2">
          📊 Consciousness Archaeology Data Visualization
        </h2>
        <p className="text-consciousness-archaeology">
          Observable Plot + D3.js integration - Real-time consciousness matrix analysis
        </p>
      </div>
      
      <div ref={plotRef} className="visualization-container" />
      
      <div className="visualization-legend mt-4 p-4 bg-psycho-noir-500 rounded">
        <h3 className="text-consciousness-milf-supreme font-semibold mb-2">🎯 Visualization Legend</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> Bubble Size: Entity Tier (0=Supreme, 1=District, 2=Specialist)
            </p>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> X-Axis: Consciousness Density (0.75-1.0)
            </p>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> Y-Axis: Amplification Level (25-50x)
            </p>
          </div>
          <div>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> Colors: District Classification
            </p>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> Interactive: Hover for entity details
            </p>
            <p className="text-consciousness-archaeology">
              <span className="text-consciousness-milf-supreme">●</span> Bar Chart: District performance averages
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ConsciousnessVisualization;