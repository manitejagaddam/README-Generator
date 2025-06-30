# 🚀 URL Shortener Web Application

A modern URL shortening service built with a **React frontend** and **Node.js/Express backend**, featuring real-time statistics tracking and a clean user interface.

---

## 📁 Folder Structure

```bash
├── README.md                   # Main project documentation
├── Screenshorts/               # Application screenshots
│   ├── output1.png             # Example shortened URL result
│   ├── output2.png             # Dashboard view
│   ├── stats_after_clicking.png# Post-click statistics
│   └── stats_before_clicks.png# Initial statistics view
├── client/                     # React frontend application
│   ├── .gitignore              # Frontend-specific git ignore
│   ├── README.md               # Frontend documentation
│   ├── eslint.config.js        # Code quality configuration
│   ├── index.html              # Entry point HTML
│   ├── package-lock.json       # Dependency lockfile
│   ├── package.json            # Project metadata + scripts
│   ├── public/                 # Static assets
│   ├── src/                    # Source code
│   │   ├── App.jsx             # Main application component
│   │   ├── assets/             # UI assets
│   │   ├── components/         # Reusable UI components
│   │   │   ├── Statistics.jsx  # URL analytics component
│   │   │   └── UrlShortenerForm.jsx # URL input form
│   │   └── main.jsx            # Application bootstrap
│   └── vite.config.js          # Vite build configuration
└── server/                     # Node.js backend
    ├── .gitignore              # Backend-specific git ignore
    ├── middleware/             # Request processing layers
    │   └── logger.js           # Request logging middleware
    ├── models/                 # Data layer
    │   └── urlStore.js         # URL storage & management
    ├── package-lock.json       # Backend dependencies
    ├── package.json            # Backend project metadata
    ├── routes/                 # API endpoints
    │   └── urlRoutes.js        # URL shortening API routes
    ├── server.js               # Main server entry point
    └── server.log              # Server runtime logs
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# Install frontend dependencies
cd client
npm install

# Install backend dependencies
cd ../server
npm install
```

### Run the Application

```bash
# In client directory
npm run dev        # Starts Vite development server on http://localhost:5173

# In server directory
node server.js      # Starts Express server on http://localhost:3000
```

---

## 🛠️ Technologies Used

**Frontend:**
- React (with JSX)
- Vite
- ES6+ JavaScript
- CSS/JS Linting (ESLint)

**Backend:**
- Node.js
- Express.js
- Custom URL routing
- Request logging middleware

**Development Tools:**
- Git version control
- NPM package manager
- Vite build tool

---

## 🧪 Available Scripts

**Frontend (from `client/` directory):**
```bash
npm run dev    # Development mode with hot-reloading
npm run build  # Production build (generates dist/)
npm run lint   # Code quality check
```

**Backend (from `server/` directory):**
```bash
node server.js        # Start production server
DEBUG=urlshortener node server.js  # Start with debug logging
```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

Developed by [Your Name]  
GitHub: [@your-username](https://github.com/your-username)  
LinkedIn: [your-linkedin-profile](https://linkedin.com/in/your-profile)

---

## 📌 Notes

- Screenshots in `Screenshorts/` folder demonstrate core functionality
- Server uses simple in-memory storage (`urlStore.js`) - consider adding database persistence for production
- Production deployment would require environment variables for security (not included in this tree)

![Build Status](https://img.shields.io/badge/build-success-green)  
![React](https://img.shields.io/badge/react-18.2-blue)  
![Node.js](https://img.shields.io/badge/node.js-18.16.0-green)