// MeetingSearch.js
import React, { useState } from 'react';

const MeetingSearch = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleSearch = (event) => {
       
        console.log(`Searching for: ${searchTerm}`);
    };

    return (
        <div>
            <h1>Search for Meetings</h1>
            <input 
                type="text" 
                placeholder="Search..." 
                value={searchTerm} 
                onChange={(e) => setSearchTerm(e.target.value)} 
            />
            <button onClick={handleSearch}>Search</button>
            {/* Render search results here */}
        </div>
    );
};

export default MeetingSearch;
