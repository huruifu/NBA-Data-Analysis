// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getDatabase } from "firebase/database";
// import { getAnalytics } from "firebase/analytics";
// import firebase from "firebase/app";
// import "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAqmnYIwGBco-yH7MLlJNkU6oi59yMsS_M",
  authDomain: "project-e1b84.firebaseapp.com",
  databaseURL: "https://project-e1b84-default-rtdb.firebaseio.com",
  projectId: "project-e1b84",
//   storageBucket: "project-e1b84.appspot.com",
//   messagingSenderId: "670316944074",
//   appId: "1:670316944074:web:607f1dc2f5dc3c700c3233",
//   measurementId: "G-YSM6GG2YQD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
// const analytics = getAnalytics(app);
// function initFirebase() {
//     if (!firebase.getApps.length) {
//         firebase.initializeApp(firebaseConfig);
//     }
// }

// initFirebase();

export { database };