import React from 'react';
import { createRoot } from 'react-dom/client';
import './Global.css'; 
import App from './App'; 
import reportWebVitals from './reportWebVitals'; 
import 'bootstrap/dist/css/bootstrap.min.css';


const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

reportWebVitals();
