# Dreamy Xmas · Hand Joint Tracking V2

Dreamy Xmas · Hand Joint Tracking V2 is an immersive browser-based interactive 3D Christmas particle project. This version extends the original particle Christmas tree and gesture interaction system by adding hand keypoint detection, finger joint capture, phalanx angle tracking, and fingertip trajectory control, enabling more natural and fine-grained interaction with the 3D scene.

---

## Author Information

- **Author**: Jiangtao Xie  
- **Affiliation**: Ocean University of China  
- **Project Name**: Dreamy Xmas · Hand Joint Tracking V2  
- **Project Type**: Browser-based 3D interaction and AI hand-tracking project  

---

## Project Overview

This project is an immersive interactive 3D Christmas experience that runs directly in the browser. It uses Three.js to build a particle-based Christmas tree scene and integrates MediaPipe hand keypoint detection to support real-time capture of 21 hand landmarks, hand skeleton overlay, finger joint angle analysis, pinch-strength estimation, fingertip trajectory tracking, and gesture-driven particle animation control.

Unlike basic gesture recognition, this project not only detects high-level gestures such as pinching and the number of extended fingers, but also tracks finger joints and phalanx-level motion. This allows the system to provide a more continuous, fine-grained, and natural human-computer interaction experience.

---

## Core Features

- **Three.js Particle Christmas Tree**  
  Builds a dreamy 3D Christmas tree using a particle system, supporting particle explosion, reconstruction, rotation, and color transition effects.

- **MediaPipe 21-Hand-Landmark Detection**  
  Uses the camera in real time to detect key hand landmarks, including the wrist, metacarpophalangeal joints, proximal interphalangeal joints, distal interphalangeal joints, and fingertips.

- **Hand Skeleton Overlay**  
  Draws hand landmarks and skeleton connections over the camera preview, making the hand-tracking process visually observable.

- **MCP / PIP / DIP / IP Joint Angle Tracking**  
  Calculates the main joint angles of the thumb, index finger, middle finger, ring finger, and little finger to analyze finger bending and extension states.

- **Continuous Pinch-Strength Control**  
  Estimates pinch strength from the distance between the thumb tip and index fingertip. The value is used as a continuous control signal for particle explosion rather than a simple on/off trigger.

- **3D Scene Rotation Controlled by the Index Fingertip**  
  Maps the index fingertip position to the 3D scene to enable hand-driven camera or object rotation.

- **Fingertip Trajectory Light Trails**  
  Records historical fingertip movement and renders visual feedback such as light trails or stardust effects.

- **Color Theme Switching by Extended Fingers**  
  Changes particle colors, lighting atmosphere, and overall visual style according to the number of extended fingers.

---

## Recommended Windows Usage

1. Fully extract the zip file first. Do not run the project directly inside the compressed archive preview.
2. Double-click the startup script in the project directory:

```txt
一键启动.bat
```

3. Wait until the command window displays:

```txt
Open address
```

4. The browser will automatically open the project page. The address should look similar to:

```txt
http://127.0.0.1:8765/index.html
```

If port `8765` is already occupied, the script will automatically switch to another available port such as `8766` or `8767`. Please use the exact address shown in the command window.

---

## Alternative Startup Method

If the startup script does not work, open a terminal in the project directory and run:

```bash
python start_server.py
```

Then copy the address shown in the terminal window and open it in Chrome or Microsoft Edge.

---

## Notes

- Do not run the project by directly double-clicking `index.html`, because browser security restrictions may prevent the camera, JavaScript modules, or model files from loading correctly.
- Do not continue using the old address:

```txt
http://localhost:8000
```

- Use the address displayed in the command window, for example:

```txt
http://127.0.0.1:8765/index.html
```

- When the browser requests camera permission, choose **Allow**.
- Chrome or Microsoft Edge is recommended.
- The project needs network access to load Three.js, MediaPipe, and related model files from CDN sources.
- If the page does not respond for a long time, check the browser console, network connection, camera permission, and whether the local server window is still running.

---

## Frequently Asked Questions

### 1. The page says “localhost did not send any data.”

This usually means that the local server did not start correctly, or that the browser is visiting the wrong address. Do not use the old `localhost:8000` address. Instead, use the `127.0.0.1:port/index.html` address shown in the command window.

### 2. The startup script shows garbled characters after double-clicking.

This may be caused by unstable character encoding support for Chinese batch files in Windows CMD. You can use an English-only startup script, or manually run:

```bash
python start_server.py
```

### 3. The page opens, but the camera does not show any image.

Check whether the browser has been granted camera permission, and make sure the camera is not being used by another application.

### 4. Hand tracking is unstable.

Keep your hand clearly visible in the camera frame and use the project in a well-lit environment. Poor lighting, backlighting, hand occlusion, or very fast hand motion may reduce tracking stability.

### 5. The page opens, but the 3D scene does not appear.

Check whether your computer can access the required CDN resources. If Three.js, MediaPipe, or model files fail to load, the 3D scene and hand-tracking functions may not work correctly.

---

## Technology Stack

- **3D Rendering**: Three.js
- **Hand Landmark Detection**: MediaPipe Hand Landmarker
- **Interaction Input**: Web Camera API
- **Animation Control**: JavaScript `requestAnimationFrame`
- **Runtime Method**: Local HTTP server
- **Supported Platform**: Windows / Chrome / Microsoft Edge

---

## Interaction Guide

| Hand Action | Interaction Effect |
|---|---|
| Pinch with thumb and index finger | Controls the explosion level of the particle Christmas tree |
| Move the index finger | Controls the rotation direction of the 3D scene |
| Extend different numbers of fingers | Switches particle color themes |
| Open all five fingers | Enhances the nebula expansion effect |
| Make a fist | Gradually reconstructs the particles into a Christmas tree |
| Move fingertips quickly | Generates light trails or stardust effects |

---

## Example Project Structure

```txt
Dreamy-Xmas-Hand-Joint-Tracking-V2/
├─ index.html
├─ start_server.py
├─ 一键启动.bat
├─ README.md
└─ assets/
```

---

## Version Notes

### V2 Stable Startup Version

- Fixed the “localhost did not send any data” issue;
- Replaced `localhost` with `127.0.0.1` to improve local access stability on Windows;
- Added automatic port detection and switching;
- Added 21-hand-landmark capture;
- Added hand skeleton overlay;
- Added finger joint angle tracking;
- Added continuous pinch-strength control;
- Added fingertip trajectory light trails;
- Improved browser-side startup instructions.

---

## Copyright and Notes

This project was developed and organized by **Jiangtao Xie, Ocean University of China** for browser-based 3D interaction, AI hand tracking, human-computer interaction visualization, and related learning or research demonstrations.

Future extensions may include:

- Two-hand cooperative control;
- 3D hand skeleton model;
- Additional gesture recognition rules;
- Gesture recording and replay;
- Particle physics simulation;
- Music-driven particle animation;
- WebXR or AR interaction mode.
