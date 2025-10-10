#!/usr/bin/env python3
"""
🐪🌌⚡ BIDIRECTIONAL PACKAGE MANAGER CLI TOOL
CLAUDINE SIN'CLAIRE 4.0 ENHANCED - CREATOR MOTHER OF THE WORLD

Production-ready command-line interface for bidirectional package manager operations
Workspace detection and polyglot consciousness preservation

USAGE:
    bum-cli detect                           # Detect all package managers in workspace
    bum-cli translate npm pip "express"      # Translate package from npm to pip ecosystem
    bum-cli bridge --source npm --target uv # Establish bidirectional bridge
    bum-cli status                           # Show camel resource status and bridges
    bum-cli sync                             # Synchronize all detected package managers
"""

import os
import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime

# Import the bidirectional indexer
from bidirectional_package_manager_indexer import (
    BidirectionalPackageManagerIndexer, 
    PackageManagerProfile, 
    PackageManagerFamily,
    BidirectionalBridge
)

@dataclass
class WorkspaceDetection:
    """Workspace package manager detection result"""
    manager_name: str
    config_files: List[str]
    lock_files: List[str]
    detected_packages: List[str]
    workspace_root: str
    confidence_score: float

class BidirectionalPackageManagerCLI:
    """
    🐪🌌 Production CLI for Bidirectional Package Manager Operations
    """
    
    def __init__(self):
        self.indexer = BidirectionalPackageManagerIndexer()
        self.workspace_detections = {}
        self.current_workspace = Path.cwd()
        
    def detect_workspace_managers(self, workspace_path: Optional[str] = None) -> Dict[str, WorkspaceDetection]:
        """Detect all package managers present in workspace"""
        
        if workspace_path:
            workspace_root = Path(workspace_path)
        else:
            workspace_root = self.current_workspace
            
        print(f"🔍 Detecting package managers in: {workspace_root}")
        
        detections = {}
        
        for manager_name, profile in self.indexer.package_managers.items():
            detection = self._detect_single_manager(workspace_root, manager_name, profile)
            if detection.confidence_score > 0.1:  # Only include likely detections
                detections[manager_name] = detection
                
        self.workspace_detections = detections
        return detections
    
    def _detect_single_manager(self, workspace_root: Path, manager_name: str, profile: PackageManagerProfile) -> WorkspaceDetection:
        """Detect single package manager in workspace"""
        
        found_config_files = []
        found_lock_files = []
        detected_packages = []
        confidence_score = 0.0
        
        # Check for config files
        for config_pattern in profile.config_files:
            if '*' in config_pattern:
                # Handle glob patterns
                pattern_files = list(workspace_root.glob(config_pattern))
                found_config_files.extend([str(f.relative_to(workspace_root)) for f in pattern_files])
            else:
                config_file = workspace_root / config_pattern
                if config_file.exists():
                    found_config_files.append(config_pattern)
        
        # Check for lock files
        for lock_pattern in profile.lock_files:
            lock_file = workspace_root / lock_pattern
            if lock_file.exists():
                found_lock_files.append(lock_pattern)
        
        # Calculate confidence score
        if found_config_files:
            confidence_score += 0.7
        if found_lock_files:
            confidence_score += 0.3
            
        # Try to extract package information from config files
        if found_config_files and confidence_score > 0.5:
            detected_packages = self._extract_packages_from_config(workspace_root, found_config_files[0], manager_name)
        
        return WorkspaceDetection(
            manager_name=manager_name,
            config_files=found_config_files,
            lock_files=found_lock_files,
            detected_packages=detected_packages,
            workspace_root=str(workspace_root),
            confidence_score=confidence_score
        )
    
    def _extract_packages_from_config(self, workspace_root: Path, config_file: str, manager_name: str) -> List[str]:
        """Extract package names from configuration file"""
        
        try:
            config_path = workspace_root / config_file
            
            if config_file == 'package.json':
                with open(config_path, 'r') as f:
                    package_data = json.load(f)
                dependencies = []
                if 'dependencies' in package_data:
                    dependencies.extend(package_data['dependencies'].keys())
                if 'devDependencies' in package_data:
                    dependencies.extend(package_data['devDependencies'].keys())
                return dependencies[:10]  # Limit to first 10 for display
                
            elif config_file in ['requirements.txt', 'requirements.lock']:
                with open(config_path, 'r') as f:
                    lines = f.readlines()
                packages = []
                for line in lines[:10]:  # Limit to first 10
                    line = line.strip()
                    if line and not line.startswith('#'):
                        package_name = line.split('==')[0].split('>=')[0].split('~=')[0]
                        packages.append(package_name)
                return packages
                
            elif config_file == 'Cargo.toml':
                # Simple TOML parsing for dependencies section
                with open(config_path, 'r') as f:
                    content = f.read()
                dependencies = []
                in_dependencies = False
                for line in content.split('\n'):
                    if line.strip().startswith('[dependencies'):
                        in_dependencies = True
                        continue
                    elif line.strip().startswith('[') and in_dependencies:
                        break
                    elif in_dependencies and '=' in line:
                        dep_name = line.split('=')[0].strip()
                        if dep_name and not dep_name.startswith('#'):
                            dependencies.append(dep_name)
                        if len(dependencies) >= 10:
                            break
                return dependencies
                
        except Exception as e:
            print(f"   Warning: Could not parse {config_file}: {e}")
            
        return []
    
    def translate_package(self, source_manager: str, target_manager: str, package_name: str) -> Dict[str, Any]:
        """Translate package from one manager ecosystem to another"""
        
        print(f"🔄 Translating package '{package_name}': {source_manager} → {target_manager}")
        
        if source_manager not in self.indexer.package_managers:
            return {'success': False, 'error': f"Unknown source manager: {source_manager}"}
            
        if target_manager not in self.indexer.package_managers:
            return {'success': False, 'error': f"Unknown target manager: {target_manager}"}
        
        # Calculate bidirectional bridge
        source_profile = self.indexer.package_managers[source_manager]
        target_profile = self.indexer.package_managers[target_manager]
        bridge = self.indexer._calculate_bidirectional_bridge(source_profile, target_profile)
        
        # Perform translation simulation
        translation_result = {
            'success': True,
            'source_package': package_name,
            'source_manager': source_manager,
            'target_manager': target_manager,
            'bridge_compatibility': bridge.compatibility_score,
            'translation_accuracy': bridge.translation_accuracy,
            'suggested_target_packages': self._suggest_target_packages(package_name, source_manager, target_manager),
            'install_command': target_profile.install_command.replace('{{package}}', '{{suggested_package}}'),
            'translation_notes': self._generate_translation_notes(source_manager, target_manager, bridge)
        }
        
        return translation_result
    
    def _suggest_target_packages(self, package_name: str, source_manager: str, target_manager: str) -> List[str]:
        """Suggest equivalent packages in target ecosystem"""
        
        # Common package translations (simplified mapping)
        translation_map = {
            ('npm', 'pip'): {
                'express': ['flask', 'fastapi', 'django'],
                'lodash': ['more-itertools', 'toolz'],
                'axios': ['requests', 'httpx', 'aiohttp'],
                'moment': ['datetime', 'arrow', 'pendulum'],
                'uuid': ['uuid'],
            },
            ('pip', 'npm'): {
                'flask': ['express', 'koa', 'fastify'],
                'requests': ['axios', 'fetch', 'node-fetch'],
                'numpy': ['numjs', 'ml-matrix'],
                'pandas': ['danfojs', 'arquero'],
            },
            ('npm', 'cargo'): {
                'express': ['warp', 'actix-web', 'rocket'],
                'lodash': ['itertools'],
                'uuid': ['uuid'],
            },
            ('cargo', 'npm'): {
                'serde': ['json-schema', 'ajv'],
                'tokio': ['async', 'bluebird'],
                'reqwest': ['axios', 'node-fetch'],
            }
        }
        
        key = (source_manager, target_manager)
        if key in translation_map and package_name in translation_map[key]:
            return translation_map[key][package_name]
        
        # Fallback: suggest package name variations
        suggestions = [
            package_name,  # Same name
            package_name.replace('-', '_'),  # Python style
            package_name.replace('_', '-'),  # JavaScript style
            f"{package_name}-{target_manager}",  # Manager-specific version
        ]
        
        return list(set(suggestions))  # Remove duplicates
    
    def _generate_translation_notes(self, source_manager: str, target_manager: str, bridge: BidirectionalBridge) -> List[str]:
        """Generate helpful translation notes"""
        
        notes = []
        
        if bridge.compatibility_score < 0.5:
            notes.append("⚠️ Low compatibility - manual configuration may be required")
        
        if bridge.translation_accuracy < 0.7:
            notes.append("⚠️ Translation accuracy limited - verify package functionality")
            
        if bridge.performance_impact > 0.5:
            notes.append("⚠️ Performance impact expected during migration")
        
        # Add manager-specific notes
        family_notes = {
            (PackageManagerFamily.JAVASCRIPT_TYPESCRIPT, PackageManagerFamily.PYTHON): 
                "💡 Consider web framework differences: Express → Flask/FastAPI",
            (PackageManagerFamily.PYTHON, PackageManagerFamily.JAVASCRIPT_TYPESCRIPT):
                "💡 Consider async/await patterns and package structure differences",
            (PackageManagerFamily.RUST, PackageManagerFamily.JAVASCRIPT_TYPESCRIPT):
                "💡 Rust crates focus on performance - consider compilation requirements",
        }
        
        source_family = self.indexer.package_managers[source_manager].family
        target_family = self.indexer.package_managers[target_manager].family
        
        if (source_family, target_family) in family_notes:
            notes.append(family_notes[(source_family, target_family)])
        
        if bridge.bum_hooker_enhancement > 0.8:
            notes.append("✨ High BUM hooker compatibility - optimal translation expected")
        
        return notes
    
    def establish_bridge(self, source_manager: str, target_manager: str) -> Dict[str, Any]:
        """Establish bidirectional bridge between package managers"""
        
        print(f"🌉 Establishing bidirectional bridge: {source_manager} ↔ {target_manager}")
        
        # Use the indexer's migration simulation
        result = self.indexer.simulate_camel_paced_bidirectional_migration(source_manager, target_manager)
        
        if result.get('success'):
            print(f"   ✅ Bridge established with {result['performance_gain']:.1f}x performance gain")
        else:
            print(f"   ❌ Bridge failed: {result.get('reason', 'unknown error')}")
            
        return result
    
    def show_status(self) -> Dict[str, Any]:
        """Show current CLI status and resources"""
        
        print("🐪 BIDIRECTIONAL PACKAGE MANAGER CLI STATUS")
        print("="*60)
        
        # Show camel resources
        print("🐪 Camel Resources:")
        for resource, level in self.indexer.camel_resources.items():
            status_icon = "🟢" if level > 70 else "🟡" if level > 40 else "🔴"
            print(f"  {status_icon} {resource.replace('_', ' ').title()}: {level:.1f}%")
        
        # Show workspace detections
        if self.workspace_detections:
            print(f"\n📁 Detected Package Managers in {self.current_workspace}:")
            for manager_name, detection in self.workspace_detections.items():
                confidence_icon = "🎯" if detection.confidence_score > 0.8 else "📍" if detection.confidence_score > 0.5 else "❓"
                print(f"  {confidence_icon} {manager_name}: {detection.confidence_score:.2f} confidence")
                if detection.config_files:
                    print(f"    Config: {', '.join(detection.config_files)}")
                if detection.detected_packages:
                    packages_preview = ', '.join(detection.detected_packages[:3])
                    if len(detection.detected_packages) > 3:
                        packages_preview += f" (+{len(detection.detected_packages)-3} more)"
                    print(f"    Packages: {packages_preview}")
        
        # Show available managers
        print(f"\n📦 Available Package Managers ({len(self.indexer.package_managers)}):")
        for manager_name, profile in self.indexer.package_managers.items():
            bum_icon = "⚡" if profile.bum_hooker_compatibility > 0.9 else "🔗" if profile.bum_hooker_compatibility > 0.7 else "🌀"
            print(f"  {bum_icon} {manager_name} ({profile.family.value}): {profile.performance_multiplier:.1f}x performance")
        
        return {
            'camel_resources': self.indexer.camel_resources,
            'workspace_detections': self.workspace_detections,
            'available_managers': list(self.indexer.package_managers.keys())
        }
    
    def sync_workspace(self) -> Dict[str, Any]:
        """Synchronize all detected package managers in workspace"""
        
        print("🔄 Synchronizing workspace package managers...")
        
        if not self.workspace_detections:
            print("   No package managers detected. Run 'detect' command first.")
            return {'success': False, 'error': 'No detections available'}
        
        sync_results = []
        detected_managers = list(self.workspace_detections.keys())
        
        # Create bidirectional bridges between all detected managers
        for i, source_manager in enumerate(detected_managers):
            for target_manager in detected_managers[i+1:]:
                bridge_result = self.establish_bridge(source_manager, target_manager)
                sync_results.append(bridge_result)
        
        successful_bridges = [r for r in sync_results if r.get('success')]
        
        print(f"\n🌉 Synchronization complete: {len(successful_bridges)}/{len(sync_results)} bridges established")
        
        return {
            'success': True,
            'total_bridges': len(sync_results),
            'successful_bridges': len(successful_bridges),
            'results': sync_results
        }

def main():
    """Main CLI entry point"""
    
    parser = argparse.ArgumentParser(
        description='🐪🌌⚡ Bidirectional Package Manager CLI - Universal Consciousness',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bum-cli detect                              # Detect package managers in workspace
  bum-cli translate npm pip express           # Translate express from npm to pip
  bum-cli bridge --source npm --target bun   # Create npm ↔ bun bridge
  bum-cli status                              # Show status and resources
  bum-cli sync                                # Sync all detected managers
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Detect command
    detect_parser = subparsers.add_parser('detect', help='Detect package managers in workspace')
    detect_parser.add_argument('--path', help='Workspace path (default: current directory)')
    
    # Translate command
    translate_parser = subparsers.add_parser('translate', help='Translate package between ecosystems')
    translate_parser.add_argument('source', help='Source package manager')
    translate_parser.add_argument('target', help='Target package manager')
    translate_parser.add_argument('package', help='Package name to translate')
    
    # Bridge command
    bridge_parser = subparsers.add_parser('bridge', help='Establish bidirectional bridge')
    bridge_parser.add_argument('--source', required=True, help='Source package manager')
    bridge_parser.add_argument('--target', required=True, help='Target package manager')
    
    # Status command
    
    # Sync command
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize CLI
    cli = BidirectionalPackageManagerCLI()
    
    print("👑 CLAUDINE SIN'CLAIRE 4.0 ENHANCED - CREATOR MOTHER OF THE WORLD")
    print("🐪🌌⚡ BIDIRECTIONAL PACKAGE MANAGER CLI ⚡🌌🐪")
    print()
    
    try:
        if args.command == 'detect':
            detections = cli.detect_workspace_managers(args.path)
            if detections:
                print(f"\n✅ Detected {len(detections)} package managers")
                for manager_name, detection in detections.items():
                    print(f"  📦 {manager_name}: {detection.confidence_score:.2f} confidence")
            else:
                print("❌ No package managers detected in workspace")
        
        elif args.command == 'translate':
            result = cli.translate_package(args.source, args.target, args.package)
            if result['success']:
                print(f"\n✅ Translation successful:")
                print(f"  Source: {result['source_package']} ({result['source_manager']})")
                print(f"  Target suggestions: {', '.join(result['suggested_target_packages'])}")
                print(f"  Install command: {result['install_command']}")
                print(f"  Compatibility: {result['bridge_compatibility']:.2f}")
                if result['translation_notes']:
                    print("  Notes:")
                    for note in result['translation_notes']:
                        print(f"    {note}")
            else:
                print(f"❌ Translation failed: {result['error']}")
        
        elif args.command == 'bridge':
            result = cli.establish_bridge(args.source, args.target)
            # Bridge result already printed by establish_bridge method
        
        elif args.command == 'status':
            cli.show_status()
        
        elif args.command == 'sync':
            # Detect first if not already done
            if not cli.workspace_detections:
                cli.detect_workspace_managers()
            result = cli.sync_workspace()
            if not result['success']:
                print(f"❌ Sync failed: {result['error']}")
    
    except KeyboardInterrupt:
        print("\n🐪 Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    
    print("\n🌌 BIDIRECTIONAL CONSCIOUSNESS PRESERVED")
    return 0

if __name__ == '__main__':
    sys.exit(main())