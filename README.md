# WildAlert

**An early-warning and decision-support concept for reducing human–wildlife conflict in Botswana.**

> **Project status: Concept and research stage.** WildAlert has not yet been implemented as a working prototype. The features and technical approach described here are proposed plans, not deployed capabilities or validated predictions.

## The problem

Human–wildlife encounters can threaten human and animal lives and cause losses involving crops, livestock, and property. Communities may not always receive timely, location-specific information that helps them prepare for potential encounters.

## The proposed solution

WildAlert is a proposed AI-assisted early-warning and decision-support platform. It aims to bring together community reports, location information, historical incident records, and—where reliable data are available—relevant environmental or sensor data. The longer-term goal is to identify potential risk areas and help communities and wildlife authorities make better-informed decisions.

WildAlert is intended to support prevention and response. It is not intended to guarantee that an encounter will be predicted or to replace advice from wildlife authorities.

## Who it is for

- Rural and wildlife-adjacent communities
- Farmers and livestock owners
- Wildlife officers and relevant authorities
- Conservation organisations and local partners
- Policymakers working on human–wildlife coexistence

## Proposed features

These are planned features; they are not yet implemented.

- **Community incident reporting:** a way for residents and farmers to report wildlife sightings or incidents, subject to privacy and safety safeguards.
- **Location-aware risk mapping:** a map that could display reported incidents and potential hotspots.
- **Risk analysis:** explore whether historical and incoming reports can support useful risk indicators or predictive models.
- **Early-warning notifications:** investigate suitable channels such as SMS or mobile notifications, depending on connectivity and partner requirements.
- **Authority-facing dashboard:** a proposed view to help wildlife officers and conservation partners review reports and prioritise responses.
- **Feedback and verification:** mechanisms for checking reports, correcting errors, and learning from outcomes.

## How it may work

1. A community member or authorised partner submits a report.
2. The report is checked for completeness and, where possible, verified.
3. The system combines suitable reports with available historical and contextual data.
4. A mapping or analysis component highlights areas that may warrant attention.
5. If evidence and testing support it, an alert may be shared with relevant users.
6. Reports, false alarms, missed events, and user feedback are reviewed to improve the approach.

This is a proposed workflow. No automated risk prediction or alert delivery is currently claimed.

## Initial focus

The concept is intended for Botswana, with further research needed to identify a suitable pilot area, data partners, reporting workflows, and community needs. Ngamiland, Chobe, Boteti, and the Okavango Panhandle have been identified as areas of interest for exploring the problem; no pilot deployment is claimed.

## Development roadmap

### Phase 1 — Discovery and validation
- Consult community members, farmers, wildlife officers, and conservation organisations.
- Understand current reporting and response pathways.
- Identify user needs, connectivity constraints, languages, and accessibility requirements.
- Map available data sources and obtain permission for any data used.
- Define safeguarding, privacy, and data-governance requirements.

### Phase 2 — Data and feasibility study
- Review the quality, coverage, and timeliness of available incident data.
- Establish a responsible method for handling location and personal information.
- Decide whether a rules-based risk indicator is more appropriate initially than machine learning.
- Define how reports and risk indicators will be verified.

### Phase 3 — Minimum viable prototype
- Build a simple demonstration for recording sample or appropriately anonymised reports.
- Display reports on a map and provide a basic review dashboard.
- Clearly label sample data and any experimental risk indicators.
- Do not issue real-world safety alerts until the system has been tested with relevant partners.

### Phase 4 — Testing and evaluation
- Test usability with intended users and partners.
- Evaluate data quality, false alarms, missed incidents, reliability, and usefulness.
- Assess whether alerts could cause harm, panic, or unsafe responses.
- Improve the system based on documented feedback.

### Phase 5 — Partner-led pilot decision
- Proceed only if local partners, data permissions, safeguards, and evaluation results support a pilot.
- Agree on responsibility for verifying reports and communicating alerts.
- Monitor outcomes and revise or stop the pilot if risks outweigh benefits.

## Safety, privacy, and responsible use

- Treat community reports as unverified until checked.
- Collect only information needed for the stated purpose and restrict access appropriately.
- Avoid publicly exposing sensitive locations, personal details, or information that could endanger people or wildlife.
- Make uncertainty clear; do not present experimental model outputs as confirmed threats.
- Design alerts with local wildlife authorities and communities so that recommended actions are safe and context-appropriate.
- Provide a way to correct inaccurate reports and review harmful or misleading outputs.

## Current status and contributions

At this stage, WildAlert is a concept being refined through research and entrepreneurship development. This repository documents the problem, proposed features, and a responsible path toward a prototype. It does not currently contain a deployed application, trained AI model, verified live data feed, or operational alert service.

Contributions such as user research, conservation expertise, data assessment, interface design, and technical prototyping may be useful as the project develops.

## Getting involved

Potential collaborators and advisors can help with:
- Human–wildlife coexistence and conservation expertise
- Community engagement and user research
- Data governance and geospatial analysis
- Software and machine-learning prototyping
- Safety evaluation and pilot design

Before sharing data or testing with communities, please contact the project lead and agree on appropriate permissions and safeguards.

## License

No license has been selected yet. Until a license is added, assume that reuse of this repository's contents is not automatically permitted.
