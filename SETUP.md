# MRCD — Environment Setup

This document covers the one-time setup steps required before running the MRCD Interactive Web Experience locally.

---

## 1. Node.js

**Required version: Node.js 18+**

The MRCD platform is built as a frontend-only React Single Page Application using Vite.

1. Ensure Node.js is installed:
   ```bash
   node -v
   ```
2. Install dependencies via npm:
   ```bash
   npm install
   ```

---

## 2. Configuration & Assets

The application logic is completely decoupled from the React codebase.
- **Content & Logic:** Driven entirely by `public/config/framework.json`.
- **Media Assets:** Ensure any required trigger media (images/video) or audio are placed in `public/media/triggers/` or `public/media/audio/`.

No database (PostgreSQL) setup or Python/backend server is required for this v1 prototype.

---

## 3. Environment Variables & API Keys

For the v1 prototype, there are **no mandatory API keys or database connection strings**. 
Because it is a static web application, all state is ephemeral and held locally in the browser session. You do not need to configure `.env` files to run the project.

---

## 4. Verify the Setup

Start the local Vite development server:

```bash
npm run dev
```

The terminal will output a local URL (usually `http://localhost:5173/`). Open this in your browser to verify the application loads.

To verify that the application compiles correctly for production deployment:
```bash
npm run build
npm run preview
```

---

*MRCD SETUP.md | Update when setup requirements change*
