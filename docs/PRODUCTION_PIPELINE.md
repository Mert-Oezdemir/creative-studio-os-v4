# Production pipeline

1. Brief the objective, audience, deliverables and brand constraints.
2. Choose one art-direction family from `style_tokens.json`.
3. Select or generate source assets and record prompt/model/version where applicable.
4. Prototype 3D in Blender; export optimized GLB for web and rendered frames for motion.
5. Create motion previews and sound design with clear editorial purpose.
6. Check aesthetic quality, visual consistency, accessibility and legal provenance.
7. Convert/export for target context (SVG, PNG, WebP, AVIF, MP4, WebM, GLB, WAV).
8. Record approvals and preserve editable masters, derivation history and source licenses.

## Blender demo

```bash
blender --background --python blender/generate_signature_scenes.py
```

Creates `signature_scenes.blend` with four labeled prototype objects and simple studio lights. This is not a cinematic render preset and must be verified with the installed Blender release.

## Important distinction

Repo web preview uses pure CSS showcase objects; the original complete offline ZIP contains additional SVG, GLB, MP4 and WAV assets not yet pushed to this repo.
