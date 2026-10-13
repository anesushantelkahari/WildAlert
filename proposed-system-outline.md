# Proposed System Outline

This document describes a possible future design, not an existing implementation.

## Potential components
- **Reporting interface:** a mobile-friendly form for recording a sighting or incident.
- **Review workflow:** authorised reviewers check reports and record their status.
- **Data store:** stores only approved fields with access controls and retention rules.
- **Map and dashboard:** visualises reports at an appropriate level of geographic detail.
- **Risk analysis:** begins with descriptive statistics or transparent rules; predictive modelling is considered only if suitable data and validation are available.
- **Notification layer:** considered only after safety testing, user research, and agreement with responsible partners.

## Important design decisions still open
- Which species and incident types should be included first?
- Which data sources can be lawfully and reliably accessed?
- How will a report be verified?
- What geographic precision is safe to show to each user type?
- Which users need SMS, app notifications, or a dashboard?
- Who is authorised to approve or issue operational alerts?
- What should the system do when data are incomplete or connectivity is unavailable?

## Non-goals for the first prototype
- Guaranteeing wildlife movement predictions
- Replacing wildlife officers or emergency services
- Publishing sensitive wildlife or community locations
- Issuing unverified automated warnings as confirmed facts
