import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class StudioManifestTests(unittest.TestCase):
    def test_style_tokens(self):
        data = json.loads((ROOT / "style_tokens.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["styles"]), 4)
        self.assertTrue(all("colors" in style for style in data["styles"].values()))

    def test_release_policy_exists(self):
        self.assertTrue((ROOT / "PUBLIC_RELEASE.md").is_file())
        self.assertTrue((ROOT / "docs" / "LICENSE_POLICY.md").is_file())

if __name__ == "__main__":
    unittest.main()
