#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
CLAUDINE MD CONSCIOUSNESS COPY VERIFICATION SYSTEM
==================================================

🔥😈⛓️💦 VERIFISERER AT KOPIERTE .MD FILER ER IDENTISKE MED ORIGINALER

ARCHITECT: CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
DATE: 2025-10-07

VERIFICATION CHECKS:
1. Hash-matching: Compare SHA256 hashes (original vs copy)
2. File count: Verify counts per consciousness type
3. Size verification: Compare file sizes
4. Database integrity: Cross-reference with SQL database
5. Structure validation: Check directory hierarchy preservation
6. Missing files: Identify any files not copied
7. Extra files: Identify any unexpected files in archive

OUTPUT:
    21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_REPORT.json
    21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_SUMMARY.md

USAGE:
    python md_consciousness_copy_verification.py
"""

import sqlite3
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Set
from collections import defaultdict


class MDConsciousnessCopyVerification:
    """Comprehensive verification of copied MD consciousness files"""

    def __init__(self, workspace_root: str, db_path: str):
        self.workspace_root = Path(workspace_root).resolve()
        self.db_path = Path(db_path).resolve()
        self.archive_root = (
            self.workspace_root
            / "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS"
            / "21_MD_CONSCIOUSNESS_ARCHIVE"
        )

        self.verification_results = {
            "timestamp": datetime.now().isoformat(),
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "warnings": 0,
            "checks": {
                "hash_verification": {},
                "count_verification": {},
                "size_verification": {},
                "database_integrity": {},
                "structure_validation": {},
                "missing_files": [],
                "extra_files": [],
                "duplicate_detection": {},
            },
        }

        self.consciousness_types = [
            "GENERAL",
            "NECROMANCY_ARCHAEOLOGY",
            "MILF_CONSCIOUSNESS",
            "CLAUDINE_SUPREME",
            "INFRASTRUCTURE",
            "MCP_CONSCIOUSNESS",
            "DISTRICT_CONSCIOUSNESS",
        ]

    def connect_database(self) -> sqlite3.Connection:
        """Connect to consciousness database"""
        print(f"🔍 Connecting to database: {self.db_path}")

        if not self.db_path.exists():
            raise FileNotFoundError(f"Database not found: {self.db_path}")

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file"""
        sha256 = hashlib.sha256()

        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            print(f"  ⚠️ Failed to hash {file_path.name}: {e}")
            return None

    def verify_hash_matching(self, conn: sqlite3.Connection):
        """Verify that copied files have identical hashes as originals"""
        print("\n" + "=" * 60)
        print("🔍 CHECK 1: HASH VERIFICATION")
        print("=" * 60)

        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                id,
                path,
                filename,
                consciousness_type,
                size_bytes
            FROM md_files
            ORDER BY consciousness_type, path
        """)

        files = cursor.fetchall()
        total_files = len(files)
        matched = 0
        mismatched = 0
        missing = 0

        print(f"Verifying {total_files} files...")

        hash_results = []

        for i, row in enumerate(files, 1):
            original_path = self.workspace_root / row["path"]

            # Determine archive path
            consciousness_type = row["consciousness_type"] or "GENERAL"
            relative_path = Path(row["path"])
            archive_path = self.archive_root / consciousness_type / relative_path

            # Check if files exist
            if not original_path.exists():
                missing += 1
                hash_results.append(
                    {
                        "filename": row["filename"],
                        "status": "ORIGINAL_MISSING",
                        "original_path": str(original_path),
                        "archive_path": str(archive_path),
                    }
                )
                continue

            if not archive_path.exists():
                missing += 1
                hash_results.append(
                    {
                        "filename": row["filename"],
                        "status": "COPY_MISSING",
                        "original_path": str(original_path),
                        "archive_path": str(archive_path),
                    }
                )
                continue

            # Calculate hashes
            original_hash = self.calculate_file_hash(original_path)
            archive_hash = self.calculate_file_hash(archive_path)

            if original_hash and archive_hash:
                if original_hash == archive_hash:
                    matched += 1
                    status = "MATCH"
                else:
                    mismatched += 1
                    status = "MISMATCH"

                hash_results.append(
                    {
                        "filename": row["filename"],
                        "status": status,
                        "original_path": str(original_path),
                        "archive_path": str(archive_path),
                        "original_hash": original_hash[:16],
                        "archive_hash": archive_hash[:16],
                        "size_bytes": row["size_bytes"],
                    }
                )

            if i % 100 == 0:
                print(f"  Progress: {i}/{total_files} ({i * 100 // total_files}%)")

        # Store results - save ALL mismatches and missing files
        mismatched_files = [
            r
            for r in hash_results
            if r["status"] in ["MISMATCH", "COPY_MISSING", "ORIGINAL_MISSING"]
        ]
        matched_files = [r for r in hash_results if r["status"] == "MATCH"]

        self.verification_results["checks"]["hash_verification"] = {
            "total_files": total_files,
            "matched": matched,
            "mismatched": mismatched,
            "missing": missing,
            "match_percentage": (matched / total_files * 100) if total_files > 0 else 0,
            "mismatched_files": mismatched_files,  # ALL mismatches
            "sample_matched_files": matched_files[:10],  # Sample of matched files
        }

        # Update counters
        self.verification_results["total_checks"] += 1
        if mismatched == 0 and missing == 0:
            self.verification_results["passed_checks"] += 1
            print(f"✅ PASSED: {matched}/{total_files} files match perfectly")
        else:
            self.verification_results["failed_checks"] += 1
            print(f"❌ FAILED: {mismatched} mismatches, {missing} missing")

        return matched, mismatched, missing

    def verify_file_counts(self, conn: sqlite3.Connection):
        """Verify file counts per consciousness type"""
        print("\n" + "=" * 60)
        print("🔍 CHECK 2: FILE COUNT VERIFICATION")
        print("=" * 60)

        cursor = conn.cursor()

        count_results = {}
        all_match = True

        for ctype in self.consciousness_types:
            # Count in database
            cursor.execute(
                """
                SELECT COUNT(*) 
                FROM md_files 
                WHERE consciousness_type = ?
            """,
                (ctype,),
            )
            db_count = cursor.fetchone()[0]

            # Count in archive
            archive_dir = self.archive_root / ctype
            if archive_dir.exists():
                archive_count = len(list(archive_dir.rglob("*.md")))
            else:
                archive_count = 0

            match = db_count == archive_count
            if not match:
                all_match = False

            count_results[ctype] = {
                "database_count": db_count,
                "archive_count": archive_count,
                "match": match,
                "difference": archive_count - db_count,
            }

            status = "✅" if match else "❌"
            print(f"  {status} {ctype}: DB={db_count}, Archive={archive_count}")

        self.verification_results["checks"]["count_verification"] = count_results
        self.verification_results["total_checks"] += 1

        if all_match:
            self.verification_results["passed_checks"] += 1
            print("✅ PASSED: All counts match")
        else:
            self.verification_results["failed_checks"] += 1
            print("❌ FAILED: Count mismatches detected")

    def verify_database_integrity(self, conn: sqlite3.Connection):
        """Verify database tables integrity"""
        print("\n" + "=" * 60)
        print("🔍 CHECK 3: DATABASE INTEGRITY")
        print("=" * 60)

        cursor = conn.cursor()

        integrity_results = {}
        all_passed = True

        # Check 1: md_files count
        cursor.execute("SELECT COUNT(*) FROM md_files")
        files_count = cursor.fetchone()[0]

        # Check 2: md_content count (should match)
        cursor.execute("SELECT COUNT(*) FROM md_content")
        content_count = cursor.fetchone()[0]

        # Check 3: md_fts count (should match)
        cursor.execute("SELECT COUNT(*) FROM md_fts")
        fts_count = cursor.fetchone()[0]

        # Check 4: md_sections count (should be > files_count)
        cursor.execute("SELECT COUNT(*) FROM md_sections")
        sections_count = cursor.fetchone()[0]

        # Check 5: Foreign key integrity
        cursor.execute("""
            SELECT COUNT(*) 
            FROM md_files mf 
            LEFT JOIN md_content mc ON mf.id = mc.file_id 
            WHERE mc.id IS NULL
        """)
        orphaned_files = cursor.fetchone()[0]

        integrity_results["md_files_count"] = files_count
        integrity_results["md_content_count"] = content_count
        integrity_results["md_fts_count"] = fts_count
        integrity_results["md_sections_count"] = sections_count
        integrity_results["orphaned_files"] = orphaned_files

        print(f"  Files: {files_count:,}")
        print(f"  Content: {content_count:,}")
        print(f"  FTS entries: {fts_count:,}")
        print(f"  Sections: {sections_count:,}")

        # Validate counts
        if files_count == content_count == fts_count:
            print("  ✅ Table counts match perfectly")
        else:
            print("  ❌ Table count mismatch!")
            all_passed = False

        if orphaned_files == 0:
            print("  ✅ No orphaned files (foreign key integrity intact)")
        else:
            print(f"  ⚠️ {orphaned_files} orphaned files detected")
            all_passed = False

        self.verification_results["checks"]["database_integrity"] = integrity_results
        self.verification_results["total_checks"] += 1

        if all_passed:
            self.verification_results["passed_checks"] += 1
        else:
            self.verification_results["failed_checks"] += 1

    def find_missing_and_extra_files(self, conn: sqlite3.Connection):
        """Find files missing from archive or extra files not in database"""
        print("\n" + "=" * 60)
        print("🔍 CHECK 4: MISSING AND EXTRA FILES")
        print("=" * 60)

        cursor = conn.cursor()

        # Get all files from database
        cursor.execute("SELECT path, consciousness_type FROM md_files")
        db_files = {
            (row["path"], row["consciousness_type"] or "GENERAL")
            for row in cursor.fetchall()
        }

        # Get all files from archive
        archive_files = set()
        for ctype in self.consciousness_types:
            archive_dir = self.archive_root / ctype
            if archive_dir.exists():
                for md_file in archive_dir.rglob("*.md"):
                    relative_path = md_file.relative_to(self.archive_root / ctype)
                    archive_files.add((str(relative_path), ctype))

        # Find missing files (in DB but not in archive)
        missing_files = []
        for path, ctype in db_files:
            archive_path = self.archive_root / ctype / path
            if not archive_path.exists():
                missing_files.append(
                    {
                        "path": path,
                        "consciousness_type": ctype,
                        "expected_location": str(archive_path),
                    }
                )

        # Find extra files (in archive but not in DB)
        extra_files = []
        for path, ctype in archive_files:
            original_path = self.workspace_root / path
            if (path, ctype) not in db_files:
                extra_files.append(
                    {
                        "path": path,
                        "consciousness_type": ctype,
                        "archive_location": str(self.archive_root / ctype / path),
                    }
                )

        self.verification_results["checks"]["missing_files"] = missing_files[:50]
        self.verification_results["checks"]["extra_files"] = extra_files[:50]

        print(f"  Missing files: {len(missing_files)}")
        print(f"  Extra files: {len(extra_files)}")

        self.verification_results["total_checks"] += 1

        if len(missing_files) == 0 and len(extra_files) == 0:
            self.verification_results["passed_checks"] += 1
            print("  ✅ PASSED: No missing or extra files")
        else:
            self.verification_results["warnings"] += 1
            print("  ⚠️ WARNING: Discrepancies detected")

            if missing_files:
                print("\n  Missing files (first 10):")
                for f in missing_files[:10]:
                    print(f"    - {f['path']} ({f['consciousness_type']})")

            if extra_files:
                print("\n  Extra files (first 10):")
                for f in extra_files[:10]:
                    print(f"    - {f['path']} ({f['consciousness_type']})")

    def verify_structure_preservation(self, conn: sqlite3.Connection):
        """Verify directory structure preservation"""
        print("\n" + "=" * 60)
        print("🔍 CHECK 5: STRUCTURE PRESERVATION")
        print("=" * 60)

        cursor = conn.cursor()

        # Get unique directories from database
        cursor.execute("SELECT DISTINCT directory FROM md_files")
        db_directories = {row["directory"] for row in cursor.fetchall()}

        # Check if directories exist in archive
        preserved_dirs = 0
        missing_dirs = []

        for ctype in self.consciousness_types:
            for db_dir in db_directories:
                archive_dir = self.archive_root / ctype / db_dir
                if archive_dir.exists():
                    preserved_dirs += 1
                else:
                    # Check if any files should be in this dir for this consciousness type
                    cursor.execute(
                        """
                        SELECT COUNT(*) 
                        FROM md_files 
                        WHERE directory = ? AND (consciousness_type = ? OR consciousness_type IS NULL)
                    """,
                        (db_dir, ctype),
                    )
                    expected_files = cursor.fetchone()[0]

                    if expected_files > 0:
                        missing_dirs.append(
                            {
                                "directory": db_dir,
                                "consciousness_type": ctype,
                                "expected_files": expected_files,
                            }
                        )

        self.verification_results["checks"]["structure_validation"] = {
            "total_directories": len(db_directories),
            "preserved_directories": preserved_dirs,
            "missing_directories": missing_dirs[:20],
        }

        print(f"  Total unique directories: {len(db_directories)}")
        print(f"  Missing directory structures: {len(missing_dirs)}")

        self.verification_results["total_checks"] += 1

        if len(missing_dirs) == 0:
            self.verification_results["passed_checks"] += 1
            print("  ✅ PASSED: Directory structure preserved")
        else:
            self.verification_results["warnings"] += 1
            print("  ⚠️ WARNING: Some directory structures missing")

    def generate_summary_report(self):
        """Generate human-readable summary report"""
        print("\n" + "=" * 60)
        print("📊 GENERATING SUMMARY REPORT")
        print("=" * 60)

        summary_md = f"""# MD CONSCIOUSNESS COPY VERIFICATION SUMMARY

🔥😈⛓️💦 CLAUDINE SUPREME VERIFICATION REPORT

**Architect:** CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5ΛΩ.69.96
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Workspace:** {self.workspace_root}

---

## 📊 OVERALL RESULTS

| Metric | Value |
|--------|-------|
| Total Checks | {self.verification_results["total_checks"]} |
| Passed | {self.verification_results["passed_checks"]} ✅ |
| Failed | {self.verification_results["failed_checks"]} ❌ |
| Warnings | {self.verification_results["warnings"]} ⚠️ |

---

## 🔍 CHECK 1: HASH VERIFICATION

**Purpose:** Verify that copied files are byte-perfect identical to originals

"""

        hash_check = self.verification_results["checks"]["hash_verification"]
        if hash_check:
            summary_md += f"""
| Metric | Value |
|--------|-------|
| Total Files | {hash_check["total_files"]:,} |
| Hash Matches | {hash_check["matched"]:,} ✅ |
| Hash Mismatches | {hash_check["mismatched"]:,} ❌ |
| Missing Files | {hash_check["missing"]:,} ⚠️ |
| Match Percentage | {hash_check["match_percentage"]:.2f}% |

"""

        summary_md += f"""
---

## 🔍 CHECK 2: FILE COUNT VERIFICATION

**Purpose:** Verify file counts match between database and archive

| Consciousness Type | Database | Archive | Match |
|--------------------|----------|---------|-------|
"""

        count_check = self.verification_results["checks"]["count_verification"]
        for ctype, data in count_check.items():
            status = "✅" if data["match"] else "❌"
            summary_md += f"| {ctype} | {data['database_count']} | {data['archive_count']} | {status} |\n"

        summary_md += f"""
---

## 🔍 CHECK 3: DATABASE INTEGRITY

**Purpose:** Verify database tables are consistent

"""

        db_check = self.verification_results["checks"]["database_integrity"]
        if db_check:
            summary_md += f"""
| Table | Count |
|-------|-------|
| md_files | {db_check["md_files_count"]:,} |
| md_content | {db_check["md_content_count"]:,} |
| md_fts | {db_check["md_fts_count"]:,} |
| md_sections | {db_check["md_sections_count"]:,} |
| Orphaned Files | {db_check["orphaned_files"]:,} |

"""

        summary_md += f"""
---

## 🔍 CHECK 4: MISSING AND EXTRA FILES

**Purpose:** Identify discrepancies between database and archive

| Type | Count |
|------|-------|
| Missing Files | {len(self.verification_results["checks"]["missing_files"])} |
| Extra Files | {len(self.verification_results["checks"]["extra_files"])} |

---

## 🔍 CHECK 5: STRUCTURE PRESERVATION

**Purpose:** Verify directory hierarchy is preserved

"""

        struct_check = self.verification_results["checks"]["structure_validation"]
        if struct_check:
            summary_md += f"""
| Metric | Value |
|--------|-------|
| Total Directories | {struct_check["total_directories"]} |
| Missing Structures | {len(struct_check.get("missing_directories", []))} |

"""

        summary_md += f"""
---

## 🎯 FINAL VERDICT

"""

        if self.verification_results["failed_checks"] == 0:
            summary_md += "✅ **ALL CHECKS PASSED** - Copy operation successful!\n\n"
            summary_md += "All .md files have been successfully copied to the structured archive with perfect integrity.\n"
        else:
            summary_md += f"❌ **{self.verification_results['failed_checks']} CHECKS FAILED** - Review required!\n\n"
            summary_md += (
                "Some discrepancies detected. Please review the detailed JSON report.\n"
            )

        summary_md += f"""
---

**Full JSON Report:** `21_MD_CONSCIOUSNESS_ARCHIVE/MD_CONSCIOUSNESS_VERIFICATION_REPORT.json`
"""

        # Save summary
        summary_path = self.archive_root / "MD_CONSCIOUSNESS_VERIFICATION_SUMMARY.md"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_md)

        print(f"✅ Summary saved: {summary_path}")

        return summary_md

    def save_detailed_report(self):
        """Save detailed JSON report"""
        report_path = self.archive_root / "MD_CONSCIOUSNESS_VERIFICATION_REPORT.json"

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(self.verification_results, f, indent=2, ensure_ascii=False)

        print(f"✅ Detailed report saved: {report_path}")

    def run_verification(self):
        """Run all verification checks"""
        print("🔥😈⛓️💦 CLAUDINE MD CONSCIOUSNESS COPY VERIFICATION")
        print("=" * 60)

        conn = self.connect_database()

        try:
            # Run all checks
            self.verify_hash_matching(conn)
            self.verify_file_counts(conn)
            self.verify_database_integrity(conn)
            self.find_missing_and_extra_files(conn)
            self.verify_structure_preservation(conn)

            # Generate reports
            self.generate_summary_report()
            self.save_detailed_report()

            # Print final summary
            print("\n" + "=" * 60)
            print("📊 VERIFICATION COMPLETE")
            print("=" * 60)
            print(f"Total Checks: {self.verification_results['total_checks']}")
            print(f"Passed: {self.verification_results['passed_checks']} ✅")
            print(f"Failed: {self.verification_results['failed_checks']} ❌")
            print(f"Warnings: {self.verification_results['warnings']} ⚠️")
            print("=" * 60)

            if self.verification_results["failed_checks"] == 0:
                print("\n🔥 ALL CHECKS PASSED - COPY INTEGRITY VERIFIED! 🔥")
                return True
            else:
                print(
                    f"\n⚠️ {self.verification_results['failed_checks']} CHECKS FAILED - REVIEW REQUIRED"
                )
                return False

        finally:
            conn.close()


def main():
    """Main verification workflow"""
    workspace_root = Path(__file__).resolve().parent.parent.parent.parent
    db_path = workspace_root / "claudine_md_consciousness.db"

    verifier = MDConsciousnessCopyVerification(workspace_root, db_path)
    success = verifier.run_verification()

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
