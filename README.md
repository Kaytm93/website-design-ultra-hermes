# Website Design Ultra — Hermes Portable

A Hermes-compatible portable Agent Plugins v1 package derived from
[Kaytm93/website-design-ultra](https://github.com/Kaytm93/website-design-ultra).

This companion package carries the 21 design skills and their progressive-
disclosure references. It is intentionally a **skills-only** port: the
Claude/Codex command files, provider-specific forward-test runners, browser
adapter, and automatic update automation from the upstream project are not
included.

## Install in Hermes

Install it from the published companion repository while keeping it disabled:

```bash
hermes plugins install <owner>/website-design-ultra-hermes --no-enable
hermes plugins doctor website-design-ultra-hermes --ci
hermes plugins enable website-design-ultra-hermes
```

Portable skills are namespaced by Hermes and are available through the normal
skill discovery and `skill_view` workflow after activation.

## Security boundary

The package contains no Python plugin code, hooks, executable scripts, MCP
configuration, environment-variable credentials, or automatic persistence.
The only active components are Markdown skills and their reference files.

## Provenance

The initial port is derived from upstream tag `v1.9.1` at commit
`b5474ccec5aed8d181aab8577d2fc3ab1a9de0b3`. Changes to the portable package are
tracked independently on the Hermes port branch.

## License

MIT. See [`LICENSE`](LICENSE).
