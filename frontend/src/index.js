import React from 'react';
import { createRoot } from 'react-dom/client';
import './Global.css'; 
import App from './App'; 
import reportWebVitals from './reportWebVitals'; 
import 'bootstrap/dist/css/bootstrap.min.css';

import axios from "axios";

axios.defaults.baseURL = "/";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

reportWebVitals();
