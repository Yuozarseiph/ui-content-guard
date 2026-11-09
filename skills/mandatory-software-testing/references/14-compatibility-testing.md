# Compatibility Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Verify required functionality across the operating systems, browsers, devices, screen sizes, runtimes, and dependency versions the product officially supports.

## 2. Prerequisites
The official support matrix MUST exist at `docs/supported-platforms.md` or an explicitly recorded approved path. If missing, BLOCKED. Relevant smoke/build prerequisites must pass.

## 3. When required
Before launch and after frontend, OS, browser, runtime, device-support, or dependency changes.

## 4. Procedure
1. Read the approved support matrix and record its version/source.
2. If no support matrix exists, STOP and set BLOCKED; do not invent supported combinations.
3. Build a test matrix covering each mandatory supported combination or the approved representative coverage strategy.
4. Execute critical workflows across supported browsers, OS versions, devices, screen sizes, and runtimes.
5. Verify layout, input, navigation, media, APIs, storage, fonts, localization, and device-specific capabilities where applicable.
6. Include the oldest supported version and documented constrained environments.
7. Record exact OS/browser/runtime versions, device, viewport, test result, and reproducible defects.

## 5. Pass criteria
- [ ] Support matrix exists and is linked.
- [ ] Every mandatory combination or approved representative combination has an execution result.
- [ ] Critical workflows pass on required supported configurations.
- [ ] Known limitations are documented and approved; unsupported combinations are not represented as supported.
- [ ] Version/device/viewport evidence is recorded.

## 6. Release gate
A failure on a required supported platform blocks launch for that platform or requires a formal support-scope decision by the appropriate human owner. Missing matrix is BLOCKED.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Default support matrix path: `docs/supported-platforms.md`.
- A reduced browser/device matrix MUST be justified by an approved coverage strategy; agents MUST NOT silently omit supported platforms.
- Compatibility PASS applies only to the tested combinations, not every possible device.

## 9. Execution record
See `00-agent-contract.md` §6.
