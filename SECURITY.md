# Security Policy

## Supported releases

Security fixes are considered for the latest maintained release. Version 1.0.0 is the initial release.

## Reporting a vulnerability

Do **not** disclose an exploitable vulnerability, private user data, credentials, or proprietary project materials in a public issue. Before this repository has a designated private reporting channel, contact a project maintainer through an existing private channel or use your hosting platform's private vulnerability-reporting feature if enabled. Do not assume a private reporting endpoint exists unless the repository publishes one.

Include a concise description, affected release, reproduction steps using synthetic data, potential impact, and suggested mitigation. Minimize sensitive details. Maintainers should acknowledge reports, investigate scope, coordinate a fix, and publish a non-sensitive summary after remediation. No response-time SLA is promised.

## Security boundaries

This skill provides **guidance**, not runtime security enforcement. It cannot independently prevent leaked UI strings, sanitize application output, secure APIs, or verify legal compliance. Treat security/privacy disclosure leaks as critical during review; enforce real protections in application code, access controls, tests, and deployment configuration.

Never use real credentials, private production records, or identifiable customer data in issue examples, tests, or documentation.
