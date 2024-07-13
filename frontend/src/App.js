// // // import logo from './logo.svg';
// // // import './App.css';

// // // function App() {
// // //   return (
// // //     <div className="App">
// // //       <header className="App-header">
// // //         <img src={logo} className="App-logo" alt="logo" />
// // //         <p>
// // //           Edit <code>src/App.js</code> and save to reload.
// // //         </p>
// // //         <a
// // //           className="App-link"
// // //           href="https://reactjs.org"
// // //           target="_blank"
// // //           rel="noopener noreferrer"
// // //         >
// // //           Learn React
// // //         </a>
// // //       </header>
// // //     </div>
// // //   );
// // // }

// // // export default App;
// // // App.js
// // import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// // import Login from './components/Login';
// // import Register from './components/Register';
// // import UserList from './components/UserList';
// // import InterestList from './components/InterestList';
// // import Chat from './components/Chat';

// // function App() {
// //   return (
// //     <Router>
// //       <Routes>
// //         <Route path="/login" element={<Login />} />
// //         <Route path="/register" element={<Register />} />
// //         <Route path="/users" element={<UserList />} />
// //         <Route path="/interests" element={<InterestList />} />
// //         <Route path="/chat/:id" element={<Chat />} />
// //       </Routes>
// //     </Router>
// //   );
// // }

// // export default App;

// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Login from './components/Login';
// import Register from './components/Register';
// import UserList from './components/UserList';
// import InterestList from './components/InterestList';
// import Chat from './components/Chat';

// function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/login" element={<Login />} />
//         <Route path="/register" element={<Register />} />
//         <Route path="/users" element={<UserList />} />
//         <Route path="/interests" element={<InterestList />} />
//         <Route path="/chat/:id" element={<Chat />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;
// src/App.js
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import UserList from './components/UserList';
import InterestList from './components/InterestList';
import Chat from './components/Chat';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/interests" element={<InterestList />} />
        <Route path="/chat/:id" element={<Chat />} />
      </Routes>
    </Router>
  );
}

export default App;
