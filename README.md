# WildAlert: AI-Powered Early Warning for Human–Wildlife Coexistence

**Using smart sensors, artificial intelligence, and timely alerts to help protect human lives, wildlife, and rural livelihoods in Botswana.**

> **Project status: Concept and design stage.** WildAlert is a proposed system. A deployed sensor network, validated wildlife-detection model, live data connection, and operational alert service have not yet been established. Metrics below are proposed pilot targets, not achieved results.

## 1. The Problem

Human–wildlife conflict threatens lives, livelihoods, food security, and biodiversity in communities living alongside wildlife corridors and protected areas. Elephants can destroy crops and damage property, while encounters involving lions, buffalo, hippos, and other wildlife can threaten people and livestock.

In some affected areas, communities may learn about nearby wildlife only after an animal has entered a settlement, approached livestock, or damaged crops. Limited connectivity, dispersed settlements, and gaps in real-time monitoring can make timely warnings difficult.

**The challenge:** How can communities and wildlife authorities detect potential wildlife threats earlier and respond before encounters become dangerous?

## 2. The Proposed Solution

WildAlert is a proposed AI-assisted, sensor-based early-warning and decision-support system designed to detect wildlife movement near selected high-risk areas and send timely alerts to affected communities, farmers, and wildlife authorities.

The proposed system combines strategically positioned sensors, AI-assisted species and movement detection, geospatial risk analysis, and accessible notifications. Rather than relying only on reports made after an encounter, WildAlert aims to identify potential risks proactively using information collected near wildlife corridors, settlement boundaries, farms, and other priority locations.

The goal is to help prevent human and animal deaths, protect livestock and crops, and support safer coexistence between communities and wildlife.

## 3. How WildAlert Will Work

### Step 1: Smart Sensor Deployment

Low-power, solar-assisted sensor units could be positioned at carefully selected locations, such as poles or suitable existing structures along wildlife corridors, near settlement boundaries, and around vulnerable agricultural areas.

Depending on field testing, cost, and permissions, units could use:
- **Camera-trap or computer-vision cameras** to capture wildlife images.
- **Passive infrared (PIR) or thermal sensors** to detect movement or heat.
- **Acoustic sensors**, where species-specific sounds provide useful evidence.
- **Location and time metadata** to associate detections with relevant geographic areas.

Sensor placement will require ecological assessment, community consultation, and permission from relevant landowners and wildlife authorities. Mounting sensors on trees may be possible at suitable sites, but the mounting method will depend on equipment, safety, tree health, and local requirements.

### Step 2: AI-Powered Detection and Analysis

When a sensor detects movement or captures an image, the system could transmit relevant data to an edge device or central processing platform, depending on connectivity and power availability.

AI models will be explored to:
- Identify wildlife species where image quality and model performance allow.
- Distinguish likely wildlife detections from false triggers.
- Analyse detection timing and repeated sightings, where the equipment supports it.
- Compare detections with nearby communities, farms, and mapped wildlife routes.
- Estimate a risk category using factors such as species, proximity, detection confidence, and the reliability of the report.

Where connectivity is limited, a future design could store detections locally and transmit them when a connection becomes available.

### Step 3: Risk Assessment and Early Warning

The platform would combine sensor detections with location data and, where available and authorised, historical incident records to identify situations that may need attention.

For example, a verified elephant detection near a crop-growing area could warrant a different response from an isolated detection far from settlements.

Risk categories must be designed and validated with wildlife experts and affected communities. The system should communicate uncertainty clearly and must not treat every detection as an imminent threat.

### Step 4: Alerts and Response

When a predefined risk threshold is met, the platform could send notifications through appropriate channels, potentially including:
- SMS alerts for communities with limited internet access.
- Mobile application notifications for registered users.
- Dashboard alerts for wildlife officers and conservation partners.
- Escalation notifications for verified high-risk incidents under agreed response protocols.

Alerts could communicate the general affected area, detection time, confidence or verification status, and recommended precautions.

Operational alert rules and response procedures would be agreed with relevant authorities. The system is not intended to replace emergency services or wildlife officers.

### Step 5: Feedback and Improvement

Authorised personnel could review detections, verify reports, and record outcomes. These records could help assess sensor performance, improve detection models, and refine risk thresholds over time.

Any model updates would require appropriate testing before being used to inform real-world alerts.

## 4. Who Will Benefit?

- **Rural communities:** Earlier warnings about potential wildlife encounters.
- **Farmers and livestock owners:** Better opportunities to protect crops, livestock, and property.
- **Wildlife officers:** More timely information to support monitoring and response planning.
- **Conservation organisations:** Better insight into recurring conflict hotspots and wildlife movement.
- **Government and policymakers:** Evidence to support human–wildlife coexistence and conservation planning.

## 5. Proposed Pilot and Impact Metrics

The first phase will assess technical feasibility and community needs before any controlled field pilot.

The following are **proposed pilot targets, not existing achievements or validated system performance**.

| Indicator | Proposed pilot target |
|---|---|
| Detection performance | Establish a baseline and aim for at least 85% recall for selected species under defined test conditions. |
| Alert delivery time | Aim to deliver an alert within 2 minutes of a qualifying detection when the system has connectivity. |
| False-alert rate | Establish a measured baseline and reduce false alerts through verification and testing. |
| System availability | Aim for at least 90% availability during an initial controlled pilot, with outages documented. |
| Community engagement | Engage at least 50 households or relevant community members in initial user research and pilot evaluation. |
| Alert comprehension | Aim for at least 80% of participating users to correctly understand an alert and its recommended response. |
| Safety and impact | Track verified incidents, near misses, false alarms, response times, and reported human, livestock, crop, and property losses. |

Targets will be reviewed against resources, species-specific performance, connectivity, safety requirements, and expert guidance. Reduced conflict or lives saved will not be claimed without appropriate evidence.

## 6. Technology and Development Roadmap

### Phase 1 — Research and validation
- Consult communities, farmers, wildlife authorities, and conservation experts.
- Identify priority species, conflict hotspots, and suitable sensor locations.
- Assess connectivity, energy requirements, data availability, and equipment costs.

### Phase 2 — Sensor and AI feasibility
- Compare camera traps, motion sensors, thermal sensing, and acoustic detection.
- Test suitable hardware and data transmission methods.
- Evaluate computer-vision models using authorised and representative wildlife data.

### Phase 3 — Minimum viable prototype
- Build a dashboard for viewing detections and incident reports.
- Connect a test sensor or clearly labelled simulated sensor feed.
- Develop an initial risk-assessment workflow and notification demonstration.
- Clearly distinguish simulated detections from real sensor observations.

### Phase 4 — Controlled field testing
- Test detection accuracy, alert latency, connectivity, power consumption, and false alarms.
- Assess performance across relevant species and environmental conditions.
- Obtain feedback from intended users and wildlife professionals.

### Phase 5 — Partner-led pilot
- Proceed only after technical validation, permissions, safety review, and partner agreement.
- Monitor system performance and community outcomes.
- Refine or discontinue components that are unreliable or could create harm.

## 7. Responsible Innovation

WildAlert is intended to support prevention, not replace local knowledge or wildlife authorities. The project will prioritise:
- Protecting sensitive wildlife-location data and community information.
- Communicating detection uncertainty clearly.
- Maintaining human oversight for consequential decisions.
- Providing safe, locally appropriate recommendations.
- Evaluating errors and potential unintended harms.
- Exploring affordable, energy-efficient technology suitable for rural settings.

## 8. Current Project Status

WildAlert is currently at the **concept and design stage**. This repository documents the proposed system architecture, intended users, development roadmap, and preliminary evaluation targets.

A functioning sensor network, trained and validated wildlife-detection model, live data connection, and operational alert service have not yet been established.

The next milestone is to develop a demonstrator that connects one test sensor—or a clearly labelled simulated sensor feed—to a dashboard and risk-assessment workflow, followed by testing with appropriate data and expert input.

## 9. Long-Term Vision

WildAlert aims to help communities and wildlife authorities move from reactive responses to more proactive, evidence-informed human–wildlife conflict prevention.

By combining appropriate sensing technology, AI-assisted analysis, and accessible early warnings, the project seeks to protect human and animal lives while supporting sustainable livelihoods and biodiversity conservation in Botswana.
