**Model**: Claude Opus 4.6

# Yantramanav — Upstream Source Investigation

## Summary

The upstream source repository for Yantramanav was identified and a source block was added to `METADATA.pb`.

## Repository

- **URL**: https://github.com/erinmclaughlin/Yantramanav
- **Owner/Designer**: Erin McLaughlin
- **Source format**: UFO (multiple masters: Thin, Light, Regular, Medium, Bold, Black)
- **Branch**: master
- **Commit**: `e40db8e44292f8e320222a37d76151b4b6bbfc7e`
- **Commit date**: 2018-01-25
- **Commit message**: "Update README.md"

## Investigation Notes

The repository was found at `erinmclaughlin/Yantramanav` and contained UFO source files in the `UFO/` directory. The DESCRIPTION.en_us.html file in google/fonts referenced this repository directly. The repository included masters for all six weights (Black, Bold, Light, Medium, Regular, Thin) as UFO directories, along with feature and spacing files. The repo is not a fork.

## Confidence

High — the repository URL is referenced in the DESCRIPTION.en_us.html of the google/fonts entry, and the designer matches the METADATA.pb attribution.
