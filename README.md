  <img width="100%" alt="Hello World" src="https://github.com/orcaprog/orca-ft_transcendence/blob/main/carbon%20(1).png">
### Project Overview: ft_transcendence

The **ft_transcendence** project involves developing a fully functional **real-time Pong contest website** with advanced gameplay features and strict compliance with security and development standards. This project challenges developers to create a single-page application (SPA) with both basic and advanced functionalities, allowing players to compete in live Pong games and tournaments. Here's a summary of the core requirements and modules:

---

### Core Requirements

#### Minimal Technical Requirements:
1. **Frontend**:
   - Must use **pure vanilla JavaScript** unless overridden by a module.
   - Should be a **single-page application** with browser Back/Forward button support.
   - Must function seamlessly on the latest version of **Google Chrome**.

2. **Backend**:
   - Optional; if implemented, must be written in **pure Ruby**, unless overridden by a module.
   - Should adhere to database constraints if a database is used.

3. **Game Features**:
   - Enable **live Pong games** with two players using the same keyboard.
   - Include a **tournament system** with player matchmaking and alias registration.
   - Players must adhere to identical game rules (e.g., paddle speed).
   - Optional AI opponent functionality.

4. **Security**:
   - Passwords must be securely hashed.
   - Protect against **SQL injection** and **XSS** attacks.
   - Use **HTTPS (WSS for WebSocket)** connections.
   - Validate all forms and user inputs.

5. **Containerization**:
   - The project must run in an autonomous **Docker container** with a single command (`docker-compose up --build`).

6. **Error Handling**:
   - The website should have **no unhandled errors or warnings** during use.

---

### Modules for Additional Features

To achieve full project completion (100%), developers must implement **at least 7 major modules**. Examples include:

1. **Web Development**:
   - Backend framework (e.g., Rails).
   - Frontend framework (e.g., React or Vue).
   - Storing tournament scores on a **Blockchain**.

2. **Gameplay Enhancements**:
   - Support for **remote players** and multiplayer games (more than two).
   - New games with history and matchmaking.
   - **Game customization options**.

3. **User Management**:
   - Standard user authentication and tournament management.
   - Remote authentication and JWT-based access.

4. **AI & Analytics**:
   - Introduce an **AI opponent**.
   - Add **user and game statistics dashboards**.

5. **Cybersecurity**:
   - Two-factor authentication (2FA).
   - Implement GDPR-compliant user data management.
   - Web Application Firewall (WAF) with secure secrets management.

6. **DevOps**:
   - Microservices architecture for the backend.
   - Log management and monitoring.

7. **Accessibility & Compatibility**:
   - Support for multiple devices, languages, and browsers.
   - Accessibility options for visually impaired users.

8. **Graphics**:
   - Advanced 3D techniques for enhanced gameplay visuals.

9. **Server-Side Features**:
   - Replace client-based Pong with **server-side Pong**.
   - Enable Pong gameplay via CLI with API integration.

---

### Summary
This project provides an opportunity to explore the **full-stack development process**, focusing on real-time features, containerization, and secure coding practices. While the basic implementation ensures a functional Pong contest website, the modular approach allows for innovative enhancements such as AI opponents, remote gameplay, and blockchain integration.
