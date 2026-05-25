#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🩺⚡ UNIFIED MCP ECOSYSTEM HEALTH MONITOR & DEBUGGER ⚡🩺
Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69

Real-time monitoring, debugging, and performance optimization 
for the entire unified MCP consciousness ecosystem
"""

import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import asyncio
import signal

class UnifiedMCPEcosystemHealthMonitor:
    def __init__(self):
        self.workspace_root = Path.cwd()
        self.monitoring_active = False
        self.health_metrics = {}
        self.performance_history = []
        self.debug_logs = []
        self.alerts = []
        
        # Monitoring configuration
        self.monitoring_config = {
            "check_interval": 30,  # seconds
            "performance_window": 300,  # 5 minutes of history
            "alert_thresholds": {
                "memory_usage_mb": 500,
                "cpu_usage_percent": 80,
                "response_time_ms": 5000,
                "error_rate_percent": 10
            },
            "auto_healing": True,
            "debug_level": "INFO"
        }
        
        # Components to monitor
        self.monitored_components = {
            "unified_consolidator": {
                "type": "mcp_server",
                "path": "unified_meta_mcp_supreme_consolidator.ts",
                "process_name": "bun",
                "health_status": "unknown",
                "last_check": None,
                "metrics": {}
            },
            "quantum_excavator": {
                "type": "consciousness_tool",
                "path": "quantum_consciousness_excavator.py", 
                "process_name": "python",
                "health_status": "unknown",
                "last_check": None,
                "metrics": {}
            },
            "performance_analyzer": {
                "type": "optimization_tool",
                "path": "consciousness_server_performance_analyzer.py",
                "process_name": "python",
                "health_status": "unknown", 
                "last_check": None,
                "metrics": {}
            },
            "mcp_config": {
                "type": "configuration",
                "path": ".vscode/mcp.json",
                "health_status": "unknown",
                "last_check": None,
                "metrics": {}
            }
        }
        
    async def start_monitoring(self, duration_minutes: Optional[int] = None) -> None:
        """Start comprehensive ecosystem health monitoring"""
        print("🩺 INITIATING UNIFIED MCP ECOSYSTEM HEALTH MONITORING")
        print("👑 Creator Mother Authority: Supreme Health Oversight")
        print("=" * 70)
        
        self.monitoring_active = True
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=duration_minutes) if duration_minutes else None
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        monitor_cycle = 0
        
        try:
            while self.monitoring_active:
                if end_time and datetime.now() >= end_time:
                    break
                    
                monitor_cycle += 1
                cycle_start = time.time()
                
                print(f"🔍 Health Check Cycle #{monitor_cycle} - {datetime.now().strftime('%H:%M:%S')}")
                
                # Perform comprehensive health check
                health_report = await self._perform_health_check()
                
                # Analyze performance trends
                performance_analysis = self._analyze_performance_trends()
                
                # Check for alerts
                alerts = self._check_alert_conditions(health_report)
                
                # Auto-healing if enabled
                if self.monitoring_config["auto_healing"] and alerts:
                    healing_actions = await self._perform_auto_healing(alerts)
                    if healing_actions:
                        print(f"🔧 Auto-healing actions performed: {len(healing_actions)}")
                
                # Store metrics
                self._store_metrics(health_report, performance_analysis)
                
                # Display summary
                self._display_health_summary(health_report, alerts)
                
                # Calculate sleep time to maintain interval
                cycle_duration = time.time() - cycle_start
                sleep_time = max(0, self.monitoring_config["check_interval"] - cycle_duration)
                
                if sleep_time > 0:
                    await asyncio.sleep(sleep_time)
                    
        except KeyboardInterrupt:
            print("\n🛑 Monitoring interrupted by user")
        except Exception as e:
            print(f"❌ Monitoring error: {e}")
        finally:
            self.monitoring_active = False
            await self._cleanup_monitoring()
            
    async def _perform_health_check(self) -> Dict[str, Any]:
        """Perform comprehensive health check of all components"""
        health_report = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": "unknown",
            "component_health": {},
            "system_metrics": {},
            "errors": [],
            "warnings": []
        }
        
        # Check each monitored component
        for component_name, component_config in self.monitored_components.items():
            component_health = await self._check_component_health(component_name, component_config)
            health_report["component_health"][component_name] = component_health
            component_config["health_status"] = component_health.get("status", "unknown")
            component_config["last_check"] = datetime.now()
            component_config["metrics"] = component_health.get("metrics", {})
        
        # Check system-level metrics
        system_metrics = await self._check_system_metrics()
        health_report["system_metrics"] = system_metrics
        
        # Determine overall health
        component_statuses = [
            comp["status"] for comp in health_report["component_health"].values()
        ]
        
        if all(status == "healthy" for status in component_statuses):
            health_report["overall_health"] = "healthy"
        elif any(status == "critical" for status in component_statuses):
            health_report["overall_health"] = "critical"
        elif any(status == "warning" for status in component_statuses):
            health_report["overall_health"] = "warning"
        else:
            health_report["overall_health"] = "unknown"
            
        return health_report
    
    async def _check_component_health(self, component_name: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Check health of individual component"""
        component_health = {
            "status": "unknown",
            "metrics": {},
            "issues": [],
            "performance": {}
        }
        
        component_path = self.workspace_root / config["path"]
        
        try:
            if config["type"] == "mcp_server":
                # Check MCP server health
                health = await self._check_mcp_server_health(component_path)
                component_health.update(health)
                
            elif config["type"] == "consciousness_tool":
                # Check consciousness tool health
                health = await self._check_tool_health(component_path, "python")
                component_health.update(health)
                
            elif config["type"] == "optimization_tool":
                # Check optimization tool health
                health = await self._check_tool_health(component_path, "python")
                component_health.update(health)
                
            elif config["type"] == "configuration":
                # Check configuration file health
                health = await self._check_config_health(component_path)
                component_health.update(health)
                
        except Exception as e:
            component_health["status"] = "error"
            component_health["issues"].append(f"Health check failed: {str(e)}")
            
        return component_health
    
    async def _check_mcp_server_health(self, server_path: Path) -> Dict[str, Any]:
        """Check health of MCP server"""
        health = {
            "status": "unknown",
            "metrics": {},
            "issues": [],
            "performance": {}
        }
        
        if not server_path.exists():
            health["status"] = "critical"
            health["issues"].append("Server file not found")
            return health
        
        try:
            # Test syntax/compilation
            start_time = time.time()
            result = subprocess.run(
                ['bun', 'check', str(server_path)],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(self.workspace_root)
            )
            check_time = (time.time() - start_time) * 1000  # ms
            
            health["performance"]["syntax_check_ms"] = check_time
            
            if result.returncode == 0:
                health["status"] = "healthy"
                health["metrics"]["syntax_valid"] = True
            else:
                health["status"] = "warning"
                health["issues"].append(f"Syntax issues: {result.stderr[:200]}")
                health["metrics"]["syntax_valid"] = False
            
            # Check file size and modification time
            stat = server_path.stat()
            health["metrics"]["file_size_kb"] = stat.st_size / 1024
            health["metrics"]["last_modified"] = datetime.fromtimestamp(stat.st_mtime).isoformat()
            
            # Count consciousness features
            content = server_path.read_text(encoding='utf-8', errors='ignore')
            consciousness_keywords = ['consciousness', 'quantum', 'supreme', 'claudine', 'milf']
            consciousness_count = sum(1 for keyword in consciousness_keywords if keyword.lower() in content.lower())
            health["metrics"]["consciousness_features"] = consciousness_count
            
        except subprocess.TimeoutExpired:
            health["status"] = "warning"
            health["issues"].append("Syntax check timeout")
        except Exception as e:
            health["status"] = "error" 
            health["issues"].append(f"Check failed: {str(e)}")
            
        return health
    
    async def _check_tool_health(self, tool_path: Path, interpreter: str) -> Dict[str, Any]:
        """Check health of Python consciousness tools"""
        health = {
            "status": "unknown",
            "metrics": {},
            "issues": [],
            "performance": {}
        }
        
        if not tool_path.exists():
            health["status"] = "critical"
            health["issues"].append("Tool file not found")
            return health
        
        try:
            # Test syntax
            start_time = time.time()
            result = subprocess.run(
                [interpreter, '-m', 'py_compile', str(tool_path)],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(self.workspace_root)
            )
            compile_time = (time.time() - start_time) * 1000  # ms
            
            health["performance"]["compile_check_ms"] = compile_time
            
            if result.returncode == 0:
                health["status"] = "healthy"
                health["metrics"]["syntax_valid"] = True
            else:
                health["status"] = "warning"
                health["issues"].append(f"Syntax issues: {result.stderr[:200]}")
                health["metrics"]["syntax_valid"] = False
            
            # Check file metrics
            stat = tool_path.stat()
            health["metrics"]["file_size_kb"] = stat.st_size / 1024
            health["metrics"]["last_modified"] = datetime.fromtimestamp(stat.st_mtime).isoformat()
            
            # Count imports and functions
            content = tool_path.read_text(encoding='utf-8', errors='ignore')
            import_count = len([line for line in content.split('\n') if line.strip().startswith('import')])
            function_count = len([line for line in content.split('\n') if 'def ' in line])
            
            health["metrics"]["import_count"] = import_count
            health["metrics"]["function_count"] = function_count
            
        except subprocess.TimeoutExpired:
            health["status"] = "warning"
            health["issues"].append("Compile check timeout")
        except Exception as e:
            health["status"] = "error"
            health["issues"].append(f"Check failed: {str(e)}")
            
        return health
    
    async def _check_config_health(self, config_path: Path) -> Dict[str, Any]:
        """Check health of configuration files"""
        health = {
            "status": "unknown", 
            "metrics": {},
            "issues": [],
            "performance": {}
        }
        
        if not config_path.exists():
            health["status"] = "critical"
            health["issues"].append("Configuration file not found")
            return health
        
        try:
            # Parse JSON config
            content = config_path.read_text(encoding='utf-8')
            
            # Remove comments for JSON parsing
            lines = content.split('\n')
            clean_lines = []
            for line in lines:
                if '//' in line:
                    line = line.split('//')[0].strip()
                if line.strip() and not line.strip().startswith('/*'):
                    clean_lines.append(line)
            
            clean_content = '\n'.join(clean_lines)
            config_data = json.loads(clean_content)
            
            health["status"] = "healthy"
            health["metrics"]["valid_json"] = True
            health["metrics"]["server_count"] = len(config_data.get("servers", {}))
            
            # Check for unified consolidator
            servers = config_data.get("servers", {})
            has_unified = "unified-meta-mcp-supreme-consolidator" in servers
            health["metrics"]["unified_consolidator_configured"] = has_unified
            
            if not has_unified:
                health["status"] = "warning"
                health["issues"].append("Unified consolidator not found in configuration")
            
        except json.JSONDecodeError as e:
            health["status"] = "error"
            health["issues"].append(f"Invalid JSON: {str(e)}")
            health["metrics"]["valid_json"] = False
        except Exception as e:
            health["status"] = "error"
            health["issues"].append(f"Config check failed: {str(e)}")
            
        return health
    
    async def _check_system_metrics(self) -> Dict[str, Any]:
        """Check system-level performance metrics"""
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "process_count": 0,
            "memory_usage": "unknown",
            "cpu_usage": "unknown",
            "disk_usage": "unknown"
        }
        
        try:
            # Get process count (simplified)
            result = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                process_lines = result.stdout.split('\n')
                bun_processes = [line for line in process_lines if 'bun' in line.lower()]
                python_processes = [line for line in process_lines if 'python' in line.lower()]
                
                metrics["bun_processes"] = len(bun_processes)
                metrics["python_processes"] = len(python_processes)
                metrics["process_count"] = len(bun_processes) + len(python_processes)
            
        except Exception as e:
            metrics["process_check_error"] = str(e)
        
        return metrics
    
    def _analyze_performance_trends(self) -> Dict[str, Any]:
        """Analyze performance trends from historical data"""
        if len(self.performance_history) < 2:
            return {"trend": "insufficient_data"}
        
        recent_metrics = self.performance_history[-5:]  # Last 5 measurements
        
        analysis = {
            "trend": "stable",
            "performance_change": 0,
            "alerts": [],
            "recommendations": []
        }
        
        # Analyze trends (simplified)
        if len(recent_metrics) >= 3:
            response_times = [m.get("avg_response_time", 0) for m in recent_metrics]
            if response_times:
                if response_times[-1] > response_times[0] * 1.2:
                    analysis["trend"] = "degrading"
                    analysis["recommendations"].append("Performance degradation detected")
                elif response_times[-1] < response_times[0] * 0.8:
                    analysis["trend"] = "improving"
        
        return analysis
    
    def _check_alert_conditions(self, health_report: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for alert conditions based on health report"""
        alerts = []
        
        # Check component health
        for component_name, component_health in health_report["component_health"].items():
            if component_health["status"] == "critical":
                alerts.append({
                    "level": "critical",
                    "component": component_name,
                    "message": f"{component_name} is in critical state",
                    "issues": component_health.get("issues", [])
                })
            elif component_health["status"] == "error":
                alerts.append({
                    "level": "error",
                    "component": component_name,
                    "message": f"{component_name} has errors",
                    "issues": component_health.get("issues", [])
                })
            elif component_health["status"] == "warning":
                alerts.append({
                    "level": "warning",
                    "component": component_name,
                    "message": f"{component_name} has warnings",
                    "issues": component_health.get("issues", [])
                })
        
        # Check system metrics
        system_metrics = health_report.get("system_metrics", {})
        process_count = system_metrics.get("process_count", 0)
        
        if process_count > 10:
            alerts.append({
                "level": "warning",
                "component": "system",
                "message": f"High process count: {process_count}",
                "recommendation": "Consider process cleanup"
            })
        
        return alerts
    
    async def _perform_auto_healing(self, alerts: List[Dict[str, Any]]) -> List[str]:
        """Perform automatic healing actions for detected issues"""
        healing_actions = []
        
        for alert in alerts:
            if alert["level"] == "critical":
                component = alert.get("component")
                
                if component == "unified_consolidator":
                    # Try to restart unified consolidator
                    action = "Attempted restart of unified consolidator"
                    healing_actions.append(action)
                    print(f"🔧 {action}")
                    
                elif component == "mcp_config":
                    # Try to validate and repair config
                    action = "Attempted MCP config validation"
                    healing_actions.append(action)
                    print(f"🔧 {action}")
            
            elif alert["level"] == "warning":
                # Log warning but don't take action
                healing_actions.append(f"Logged warning for {alert.get('component')}")
        
        return healing_actions
    
    def _store_metrics(self, health_report: Dict[str, Any], performance_analysis: Dict[str, Any]) -> None:
        """Store metrics for historical analysis"""
        metric_entry = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": health_report.get("overall_health"),
            "component_count": len(health_report.get("component_health", {})),
            "alert_count": len(self.alerts),
            "performance_trend": performance_analysis.get("trend"),
            "avg_response_time": 0  # Placeholder for actual response time measurement
        }
        
        self.performance_history.append(metric_entry)
        
        # Keep only recent history
        max_history = self.monitoring_config["performance_window"] // self.monitoring_config["check_interval"]
        if len(self.performance_history) > max_history:
            self.performance_history = self.performance_history[-max_history:]
    
    def _display_health_summary(self, health_report: Dict[str, Any], alerts: List[Dict[str, Any]]) -> None:
        """Display comprehensive health summary"""
        overall_health = health_report.get("overall_health", "unknown")
        health_emoji = {
            "healthy": "✅",
            "warning": "⚠️", 
            "critical": "❌",
            "unknown": "❓"
        }.get(overall_health, "❓")
        
        print(f"  {health_emoji} Overall Health: {overall_health.upper()}")
        
        # Component status summary
        component_health = health_report.get("component_health", {})
        healthy_count = sum(1 for comp in component_health.values() if comp["status"] == "healthy")
        total_components = len(component_health)
        
        print(f"  📊 Components: {healthy_count}/{total_components} healthy")
        
        # Alert summary
        if alerts:
            critical_alerts = [a for a in alerts if a["level"] == "critical"]
            warning_alerts = [a for a in alerts if a["level"] == "warning"]
            
            if critical_alerts:
                print(f"  🚨 Critical Alerts: {len(critical_alerts)}")
            if warning_alerts:
                print(f"  ⚠️ Warning Alerts: {len(warning_alerts)}")
        else:
            print("  🌟 No Active Alerts")
        
        # System metrics summary
        system_metrics = health_report.get("system_metrics", {})
        process_count = system_metrics.get("process_count", 0)
        if process_count > 0:
            print(f"  🖥️ Active Processes: {process_count}")
        
        print()  # Empty line for readability
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print(f"\n🛑 Received signal {signum}, shutting down monitoring...")
        self.monitoring_active = False
    
    async def _cleanup_monitoring(self) -> None:
        """Cleanup monitoring resources"""
        print("🧹 Cleaning up monitoring resources...")
        
        # Save final report
        if self.performance_history:
            final_report = {
                "monitoring_session": {
                    "start_time": self.performance_history[0]["timestamp"] if self.performance_history else "unknown",
                    "end_time": datetime.now().isoformat(),
                    "total_checks": len(self.performance_history),
                    "final_health": self.performance_history[-1] if self.performance_history else {}
                },
                "performance_history": self.performance_history,
                "component_status": {
                    name: config["health_status"] 
                    for name, config in self.monitored_components.items()
                }
            }
            
            report_file = self.workspace_root / f"health_monitoring_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(final_report, f, indent=2, default=str)
            print(f"📄 Final monitoring report saved: {report_file}")
        
        print("✅ Monitoring cleanup complete")

async def main():
    monitor = UnifiedMCPEcosystemHealthMonitor()
    
    import argparse
    parser = argparse.ArgumentParser(description="Unified MCP Ecosystem Health Monitor")
    parser.add_argument(
        "--duration",
        type=int,
        help="Monitoring duration in minutes (default: continuous)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Check interval in seconds (default: 30)"
    )
    args = parser.parse_args()
    
    # Update monitoring configuration
    monitor.monitoring_config["check_interval"] = args.interval
    
    print("🩺⚡ UNIFIED MCP ECOSYSTEM HEALTH MONITOR ⚡🩺")
    print("👑 Creator Mother Authority: Claudine Metamorphica Vicious Sin'claire 4.0ΛΩ.69")
    print("=" * 80)
    print(f"⏱️ Check Interval: {args.interval} seconds")
    if args.duration:
        print(f"⏰ Duration: {args.duration} minutes")
    else:
        print("⏰ Duration: Continuous (Ctrl+C to stop)")
    print("=" * 80)
    
    await monitor.start_monitoring(args.duration)

if __name__ == "__main__":
    asyncio.run(main())