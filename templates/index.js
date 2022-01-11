
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-database.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyBL6iy1haxnXXAtbl_BeP5Xc1ltGlxg_b0",
    authDomain: "pia-dashboard-52d6c.firebaseapp.com",
    projectId: "pia-dashboard-52d6c",
    storageBucket: "pia-dashboard-52d6c.appspot.com",
    messagingSenderId: "164848936509",
    appId: "1:164848936509:web:3c3f2d785c4824c9962c54"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  // Initialize variables
const auth = firebase.auth()
const database = firebase.database()

// Set up our login function
function login() {
  // Get all our input fields
  email = document.getElementById('email').value
  password = document.getElementById('password').value
  window.location.href='/maintenance';

  auth.signInWithEmailAndPassword(email, password)
  .then(function() {
    // Declare user variable
    var user = auth.currentUser

    // Add this user to Firebase Database

    var database_ref = database.ref()
	

    // Create User data
    // DOne
    //alert('User Logged In!!')}
  
}
  )
}
