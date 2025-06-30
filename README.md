# 🧾 LinkShortener Pro

A modern URL shortening service with real-time analytics built using React + Node.js. Features include custom short codes, click statistics tracking, and responsive UI components.

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/yourname/linkshortener-pro/main.yml?branch=main)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📁 Project Structure

```bash
.
├── README.md                   # This documentation file
├── Screenshorts/               # 📸 Demo screenshots folder
│   ├── output1.png             # Example short URL preview
│   ├── output2.png             # Dashboard view
│   ├── stats_after_clicking.png# Post-click analytics
│   └── stats_before_clicks.png# Pre-click statistics view
├── client/                     # 🌐 Frontend (React + Vite)
│   ├── .gitignore              # Frontend-specific ignores
│   ├── README.md               # Client-specific documentation
│   ├── eslint.config.js        # Code quality configuration
│   ├── index.html              # Entry point
│   ├── package.json            # Dev dependencies (React, Vite)
│   ├── public/                 # Static assets
│   ├── src/                    # Source code
│   │   ├── App.jsx             # Main component
│   │   ├── assets/             # Logo and icons
│   │   ├── components/         # Reusable UI elements
│   │   │   ├── Statistics.jsx  # Analytics component
│   │   │   └── UrlShortenerForm.jsx # URL input form
│   │   └── main.jsx            # App bootstrap
│   └── vite.config.js          # Build configuration
└── server/                     # ⚙️ Backend (Node.js + Express)
    ├── .gitignore              # Server-specific ignores
    ├── middleware/             # Request processing
    │   └── logger.js           # Request logging
    ├── models/                 # Data layer
    │   └── urlStore.js         # URL database/manager
    ├── package.json            # Server dependencies
    ├── routes/                 # API endpoints
    │   └── urlRoutes.js        # URL management routes
    ├── server.js               # Entry point
    └── server.log              # Runtime logs
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/linkshortener-pro.git
cd linkshortener-pro

# Install client dependencies
cd client
npm install

# Install server dependencies
cd ../server
npm install
```

### To Run Locally:

```bash
# Start frontend (port 5173)
cd client
npm run dev

# Start backend (port 3000)
cd ../server
npm start
```

---

## 🛠️ Technologies Used

**Frontend Stack:**
- React 18+ (with JSX)
- Vite 4 (build tool)
- ES Lint (code quality)
- Modern CSS (Tailwind/CSS-in-JS)

**Backend Stack:**
- Node.js 18+
- Express.js 5
- Express Router
- File-based storage (urlStore.js)

---

## 🧪 Available Scripts

**Client:**
```bash
npm run dev    # Development server
npm run build  # Production build
npm run lint   # Code quality check
```

**Server:**
```bash
npm start      # Production mode
npm run dev    # Development mode (with nodemon)
npm run logs   # View server.log contents
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👤 Author

Developed by [Your Name]  
LinkedIn: [your-profile](https://linkedin.com/in/yourname) | Twitter: [@yourhandle](https://twitter.com/yourhandle)

> _"Shorten links, grow your reach!"_ 🚀