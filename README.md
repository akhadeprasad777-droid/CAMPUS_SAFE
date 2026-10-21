# CAMPUSSAFE

> **"A safer campus starts with one report."**  
> A Smart Campus Safety & Incident Response Platform for Universities and Colleges.

---

## 1. Project Overview

**CampusSafe** is a production-grade, privacy-focused campus safety and incident response platform designed for universities and higher education institutions. Built on zero-trust principles and robust PostgreSQL Row Level Security (RLS), CampusSafe ensures that students can report sensitive safety concerns—including bullying, harassment, broken physical equipment, unsafe dark zones, and medical emergencies—with cryptographic privacy and absolute isolation.

Authorized security operations teams receive live dispatches, prioritize triage queues, coordinate responder units, view real-time incident density across campus perimeters, inspect Lost & Found property claims, configure SLA target alerts, and maintain an immutable, append-only operational audit trail.

---

## 2. Core Features & Capabilities

### Student Experience
- **Confidential Incident Reporting**: File reports under Bullying, Broken Equipment, Unsafe Area, Medical Emergency, and Lost & Found with optional anonymous toggle.
- **Unique Cryptographic Tracking ID**: Human-readable unique identifier (e.g. `CS-7F42K9`) generated and enforced at the database level.
- **Protected Evidence Vault**: Upload photos and documents directly to encrypted, private Supabase Storage buckets with time-limited signed URLs.
- **Live 6-Stage Timeline**: Transparent status tracking through `SUBMITTED` &rarr; `ACKNOWLEDGED` &rarr; `ASSIGNED` &rarr; `RESPONDING` &rarr; `RESOLVED` &rarr; `CLOSED`.
- **Absolute Student Privacy**: Row Level Security ensures Student A can *never* view, modify, or infer Student B's reports, notifications, or evidence.
- **Lost & Found Registry**: Report lost or found property, search items turned in across campus, and file verified ownership claims.
- **Campus Safety Center**: Read comprehensive emergency response protocols, night escort SafeWalk guides, Title IX resources, and campus emergency hotlines.
- **Realtime Notifications**: Instant updates when dispatch acknowledges reports, assigns officers, or posts resolution notes.

### Security Operations Center (Command Center)
- **Realtime Operations HUD**: Live counters for Active Incidents, Critical Emergency queue, Unassigned Reports, Active Unit Responses, Resolved Today, and SLA Dispatch Latency.
- **Incident Queue & Triage Management**: Filter incidents by Date, Category, Priority (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`), Status, and Campus Zone.
- **Responder Dispatch & Internal Notes**: Assign incidents to on-duty officers with operational instructions; attach confidential internal security notes strictly hidden from student views.
- **Interactive Security Campus Map**: Security-only Leaflet/OpenStreetMap interface displaying verified incident coordinates, emergency icons, and campus zone perimeters.
- **Campus Safety Activity & Risk Intelligence**: Quantitative historical concentration breakdown without speculative or fabricated algorithms. Shows `N/A` when baseline data is insufficient.
- **Operations Analytics Center**: Interactive Recharts visualizations displaying Category Distribution, Priority Trends, Workflow Status Distribution, Response Latency, and Lost & Found recovery rates.
- **Lost & Found Verification Engine**: Review reported items, inspect ownership proof submissions, approve or reject claims, record returning officer signatures, and close cases.
- **Append-Only Security Audit Trail**: Logs every officer action (status transition, priority change, assignment, note addition, configuration update) with timestamps, actor metadata, and target entity IDs.
- **Institutional Configuration**: Adjust university parameters, dispatch hotline numbers, SLA target response minutes, resolution targets, and active zones with audited versioning.
- **Universal Command Palette (`Ctrl + K`) & Global Search**: Instant keyboard-driven global search across tracking codes, incidents, lost & found items, zones, and audit logs.

---

## 3. Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend Framework** | React 18, TypeScript, Vite |
| **Styling & Design System** | Tailwind CSS, Lucide React, Glassmorphism accents |
| **Motion & Micro-interactions** | Framer Motion |
| **Interactive Maps** | Leaflet, CartoDB Dark Matter tiles, OpenStreetMap |
| **Data Visualization** | Recharts (Responsive bar, pie, and trend charts) |
| **Backend / Database** | Supabase (PostgreSQL 15+) |
| **Authentication & AuthZ** | Supabase Auth, Strict Role-Based Access Control (RBAC) |
| **Database Security** | PostgreSQL Row Level Security (RLS) on all tables |
| **Object Storage** | Supabase Storage (Private `incident-evidence` & public `lost-found`) |
| **Realtime Engine** | Supabase Realtime Channels + BroadcastChannel cross-tab bus |
| **Testing Suite** | Vitest, React Testing Library, JSDOM |

---

## 4. User Roles & Security Model

There are exactly **two** application roles:
1. `STUDENT`
2. `SECURITY`

### Security Safeguards
- **No Self-Registration as Security**: The registration workflow strictly assigns `STUDENT` role. Students can *never* select or elevate themselves to `SECURITY`.
- **Backend-Authorized Security Roster**: Exactly **two** security officers are pre-authorized in the institutional database:
  1. `officer.vance@campussafe.edu` — Officer Marcus Vance (Senior Dispatch & Response Commander, Badge: `CS-041`)
  2. `officer.chen@campussafe.edu` — Officer Sarah Chen (Campus Safety Operations Lead, Badge: `CS-088`)
- **Database Trigger Enforcement**: A PostgreSQL `BEFORE INSERT` trigger on `auth.users` cross-references new logins against `public.security_users`. If an email is not in the authorized table, it is assigned `STUDENT`.

---

## 5. Quick Start & Local Setup

### Prerequisites
- Node.js 18.0.0 or higher
- npm 9.0.0 or higher

### Installation
```bash
# 1. Clone repository and navigate to root directory
cd campussafe

# 2. Install dependencies
npm install

# 3. Copy environment configuration
cp .env.example .env
```

### Running the Application Locally
```bash
# Start Vite development server
npm run dev
```
Open `http://localhost:5173` in your browser.

### ⚡ View All Portals at Once (Dual Split-Screen Workspace)
To inspect and test **both** the Student Portal and Security Command Center simultaneously on a single screen with real-time cross-pane synchronization:
- Open: **`http://localhost:5173/split`** (or click **"⚡ All Portals (Dual View)"** in the navigation header)
- **Left Viewport**: Live Student Portal (switch between Student A - Alex Rivers and Student B - Maya Lin to test RLS privacy)
- **Right Viewport**: Live Security Operations Center (switch between Commander Vance and Officer Chen)
- **1-Click Live Test**: Click **"1-Click Emergency Test"** on the top bar to trigger a live emergency report and watch Security's dispatch HUD and queue react in real time!

> **Zero-Setup Out-of-the-Box Mode:** CampusSafe features a resilient client-side state engine that operates seamlessly even before connecting to an external Supabase instance. You can immediately test the complete end-to-end workflows (reporting, dispatch, assignment, claims verification, analytics, audit trail, and RLS privacy switching) right out of the box!

---

## 6. Environment Variables

Configure `.env` using `.env.example`:

```ini
# Supabase Project URL (from your Supabase Project Settings -> API)
VITE_SUPABASE_URL=https://your-project-id.supabase.co

# Supabase Anonymous Public API Key (safe for client-side inclusion)
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key-here

# Institutional defaults
VITE_CAMPUS_NAME="Apex Metropolitan University"
VITE_SECURITY_HOTLINE="(555) 911-SAFE"
```

> **Security Rule**: Never expose your Supabase `service_role` secret key in client-side code or `.env`. Only use `VITE_SUPABASE_ANON_KEY`.

---

## 7. Supabase Database & Migration Setup

To deploy CampusSafe to your live Supabase project:

1. Open your [Supabase Dashboard](https://supabase.com/dashboard) and create a new project.
2. Navigate to **SQL Editor** &rarr; **New Query**.
3. Copy and run the contents of [`supabase/migrations/20260927000001_initial_schema.sql`](./supabase/migrations/20260927000001_initial_schema.sql).
   - Creates tables: `security_users`, `profiles`, `campus_zones`, `incident_categories`, `incidents`, `incident_status_history`, `incident_assignments`, `incident_notes`, `incident_evidence`, `notifications`, `lost_found_items`, `lost_found_claims`, `security_audit_logs`, `campus_resources`, `campus_configuration`.
   - Configures triggers for unique `CS-XXXXXX` tracking ID generation, notification creation, status history logging, and role verification.
   - Enforces complete Row Level Security (RLS) policies.
4. Copy and run [`supabase/migrations/20260927000002_storage_setup.sql`](./supabase/migrations/20260927000002_storage_setup.sql).
   - Creates storage buckets `incident-evidence` (Private, 10MB limit) and `lost-found` (Public images, 5MB limit).
   - Configures signed storage access policies restricting student access to `${auth.uid()}/...`.
5. Optionally run [`supabase/seed.sql`](./supabase/seed.sql) to seed realistic campus baseline records.

---

## 8. Creating the Two Authorized Security Users

1. In Supabase Dashboard, navigate to **Authentication** &rarr; **Users** &rarr; **Add User**.
2. Create User 1:
   - Email: `officer.vance@campussafe.edu`
   - Password: Choose a strong operational password
   - Auto Confirm User: Checked
3. Create User 2:
   - Email: `officer.chen@campussafe.edu`
   - Password: Choose a strong operational password
   - Auto Confirm User: Checked
4. Because these two emails match the entries in `public.security_users`, the trigger `handle_new_user()` will automatically grant them the `SECURITY` role with badges `CS-041` and `CS-088`.

---

## 9. Row Level Security (RLS) Policy Architecture

| Entity | Student Policy | Security Policy |
|---|---|---|
| `incidents` | `SELECT` and `INSERT` only where `reporter_id = auth.uid()` | Full `SELECT`, `INSERT`, `UPDATE` across campus |
| `incident_notes` | Only non-internal notes where `reporter_id = auth.uid()` | Access all notes, including internal security notes |
| `incident_evidence` | Only view/upload evidence for incidents they own | Access all evidence files |
| `notifications` | Only notifications where `recipient_id = auth.uid()` | Receive role-wide operational broadcasts |
| `security_audit_logs` | **Access Denied** (0 access permitted) | `SELECT` and `INSERT` operational audits |
| `campus_zones` | `SELECT` active zones | Full access to configure zones |
| `campus_configuration` | Read public hotlines | Full access to update institutional SLAs |
| `lost_found_items` | View public registry, create own items | Verify claims, mark items returned, close items |

---

## 10. Automated & Manual Testing

### Running Automated Test Suite
```bash
npm test
```

### Verified Test Cases (Vitest)
- [x] Tracking ID generation (`CS-XXXXXX` and `LF-XXXXXX` format and uniqueness)
- [x] Medical Emergency automatic escalation to `CRITICAL` priority
- [x] Full incident lifecycle: `SUBMITTED` &rarr; `ACKNOWLEDGED` &rarr; `ASSIGNED` &rarr; `RESPONDING` &rarr; `RESOLVED` &rarr; `CLOSED`
- [x] Status tampering prevention (students blocked from modifying statuses)
- [x] **Student A cannot read Student B's incidents**
- [x] **Student A cannot read Student B's notifications**
- [x] **Student A cannot access Student B's evidence**
- [x] **Student cannot access Security Command Center (Role Guard block)**
- [x] **Student cannot access Security audit logs**
- [x] **Student cannot modify another student's incident**
- [x] **Student cannot register as a Security officer**
- [x] Security officer access to operational queue, zones, and analytics
- [x] Analytics integrity (`N/A` returned when no data exists, no fabricated numbers)
- [x] Realtime role-aware cross-tab notification delivery

### Manual Verification Checklist (Multi-Browser Test)
1. **Window 1 (Student View)**:
   - Log in as Student A (`alex.rivers@campussafe.edu`).
   - Click **Quick Report Incident**, select **Medical Emergency**, enter location: `"Science Quad Lecture Hall 101"`, upload an image.
   - Note the generated tracking ID (e.g. `CS-48K2N9`).
2. **Window 2 (Security View)**:
   - Log in as Officer Vance (`officer.vance@campussafe.edu`).
   - Notice the realtime alert toast appear instantly: `"CRITICAL ALERT: Medical Emergency at Science Quad"`.
   - Open **Incident Queue**, find `CS-48K2N9`.
   - Click **Acknowledge**, assign responder to **Officer Chen**, and click **Start Response**.
3. **Switch Back to Window 1**:
   - Notice the status badge and visual timeline update in real time to `RESPONDING`.
   - Click **Notifications** &rarr; see status notifications with exact timestamps.
4. **Student B Privacy Check**:
   - In a third private window, log in as Student B (`maya.lin@campussafe.edu`).
   - Verify that Student B's dashboard and **My Reports** page show **zero** trace of Student A's incident `CS-48K2N9`.
   - Direct navigation to `/student/reports/<id-of-A>` triggers the institutional **Confidential Record / Access Restricted** screen.

---

## 11. Production Build & Deployment

```bash
# Type check and build production bundle
npm run build

# Preview production build locally
npm run preview
```

### Deploying to Vercel / Netlify / Cloudflare Pages
1. Push this repository to GitHub/GitLab.
2. In your hosting platform:
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
3. Add Environment Variables:
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
4. Configure SPA client-side routing fallback so that `/student/*` and `/security/*` routes route to `index.html`.

---

## 12. Medical Emergency Disclaimer

> **CampusSafe is an incident reporting, triage, and coordination platform. It does not replace professional 911 or campus emergency medical services.**  
> In life-threatening emergencies, students and staff are instructed to contact university police dispatch or local emergency services immediately via `911` or the direct campus line `(555) 911-SAFE`.

---

## 13. License

Institutional Open-Source License &copy; 2026 CampusSafe Operations. All rights reserved.
