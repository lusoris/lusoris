### Hi, I'm Kilian

**Open-source tooling for video quality, Go and SvelteKit frameworks, and for keeping fleets of coding agents honest.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=go,py,c,rust,ts,svelte,kubernetes,linux&perline=8&theme=dark">
  <img src="https://skillicons.dev/icons?i=go,py,c,rust,ts,svelte,kubernetes,linux&perline=8&theme=light" alt="Go, Python, C, Rust, TypeScript, Svelte, Kubernetes, Linux" height="44">
</picture>

[![Merged upstream](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Flusoris%2Flusoris%2Fmain%2Fupstream.json&query=%24.merged_total&label=merged%20upstream&color=2ea44f)](#upstream)

Most of the work lives in a few organisations:

| Area | Project | What it is |
| :-- | :-- | :-- |
| Video | [VMAFx](https://github.com/VMAFx/vmafx) | Perceptual video quality assessment (VMAF), GPU-accelerated and SIMD-tuned, every backend checked against the CPU scores |
| Video | [ffmpeg-patches](https://github.com/VMAFx/ffmpeg-patches) | A shared series of FFmpeg fixes, tracked against FFmpeg master and sent upstream |
| Go | [golusoris](https://github.com/golusoris/golusoris) | A composable Go framework: opt-in modules for what a production backend needs |
| Go | [goenvoy](https://github.com/golusoris/goenvoy) | Go client libraries for media automation, metadata and download APIs |
| Web | [sveltesentio](https://github.com/golusoris/sveltesentio) | A composable SvelteKit framework with opt-in modules |
| Agents | [Praetor](https://github.com/cordanaLLM/praetor) | Repository rules as code and one engine that holds every coding agent to them |
| Systems | [nucleus](https://github.com/cordanaLLM/nucleus) | A deterministic Linux kernel build with hardened configuration fragments |
| Media | [SnatchArr](https://github.com/lusoris/SnatchArr) | Finds missing media across *arr instances while respecting hourly caps |

### Upstream

Fixes that left my own trees and were merged where they belong:

<!-- upstream:start -->
[![FFmpeg: 1 merged](https://img.shields.io/badge/FFmpeg-1%20merged-2ea44f?logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![OpenVINO Model Server: 2 merged](https://img.shields.io/badge/OpenVINO%20Model%20Server-2%20merged-2ea44f?logo=openvino&logoColor=white)](https://github.com/openvinotoolkit/model_server)
[![Vulkan Validation Layers: 1 merged](https://img.shields.io/badge/Vulkan%20Validation%20Layers-1%20merged-2ea44f?logo=vulkan&logoColor=white)](https://github.com/KhronosGroup/Vulkan-ValidationLayers)
[![Paperclip: 1 merged](https://img.shields.io/badge/Paperclip-1%20merged-2ea44f)](https://github.com/paperclipai/paperclip)
[![Paperclip Aperture: 1 merged](https://img.shields.io/badge/Paperclip%20Aperture-1%20merged-2ea44f)](https://github.com/tomismeta/paperclip-aperture)
[![Hindsight: 1 merged](https://img.shields.io/badge/Hindsight-1%20merged-2ea44f)](https://github.com/vectorize-io/hindsight)

| Project | Merged |
| :-- | --: |
| [FFmpeg](https://ffmpeg.org/) | 1 |
| [OpenVINO Model Server](https://github.com/openvinotoolkit/model_server) | 2 |
| [Vulkan Validation Layers](https://github.com/KhronosGroup/Vulkan-ValidationLayers) | 1 |
| [Paperclip](https://github.com/paperclipai/paperclip) | 1 |
| [Paperclip Aperture](https://github.com/tomismeta/paperclip-aperture) | 1 |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 1 |
<!-- upstream:end -->

More are in review. I report what I find with a reproduction and a measurement, and I send the fix
when I have one.

### Working with me

- Bug reports with a reproduction are the fastest way to get something fixed.
- Every project states its licence and credits what it builds on.
- Questions about a project go to that project's discussions.

<sub>My avatar is a character in the style of the Go gopher. The Go gopher was designed by Renee French
and is licensed under the Creative Commons Attribution 4.0 licence. The tech icons come from
<a href="https://github.com/tandpfun/skill-icons">skill-icons</a> (MIT). The upstream section is generated from
<a href="upstream.json">upstream.json</a> by <a href="tools/render.py">tools/render.py</a>.</sub>
