from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "3d-art-direction",
    "3d-asset-pipeline",
    "3d-runtime-quality",
    "anti-slop",
    "canvas-first-architecture",
    "color-palettes",
    "component-patterns",
    "content-design",
    "core-rules",
    "immersive-3d",
    "loading-choreography",
    "motion-system",
    "r3f-interaction",
    "r3f-patterns",
    "render-graph",
    "scroll-immersion",
    "shaders-tsl",
    "spatial-audio",
    "style-directions",
    "typography",
    "ui-states",
}


class PortablePackageTests(unittest.TestCase):
    def test_root_manifest_uses_agent_plugins_v1(self) -> None:
        manifest_path = ROOT / "plugin.json"
        self.assertTrue(manifest_path.is_file())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(
            manifest["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        self.assertEqual(manifest["name"], "website-design-ultra-hermes")
        self.assertEqual(manifest["version"], "1.9.1")
        self.assertEqual(manifest["license"], "MIT")

    def test_all_expected_skills_are_at_package_root(self) -> None:
        skills_root = ROOT / "skills"
        self.assertEqual(
            {path.name for path in skills_root.iterdir() if path.is_dir()},
            EXPECTED_SKILLS,
        )
        for skill_name in EXPECTED_SKILLS:
            skill_md = skills_root / skill_name / "SKILL.md"
            self.assertTrue(skill_md.is_file(), skill_name)
            content = skill_md.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"), skill_name)
            match = re.search(r"\nname:\s*([^\n]+)\n", content)
            if match is None:
                self.fail(skill_name)
            self.assertEqual(match.group(1).strip(), skill_name)
            self.assertRegex(content, r"\ndescription:\s*.+\n", skill_name)

    def test_portable_package_contains_no_automatic_persistence_or_provider_scripts(self) -> None:
        forbidden_paths = [ROOT / "commands", ROOT / "scripts", ROOT / ".claude-plugin", ROOT / ".codex-plugin"]
        for path in forbidden_paths:
            self.assertFalse(path.exists(), path)
        for path in ROOT.rglob("*"):
            if "tests" in path.parts:
                continue
            if path.is_file() and path.suffix in {".sh", ".mjs", ".js", ".py"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                self.assertNotIn("launchctl", text.lower(), path)
                self.assertNotIn("launchagents", text.lower(), path)


if __name__ == "__main__":
    unittest.main()
