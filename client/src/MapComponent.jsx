import React, { useState, useEffect } from 'react';

export default function MapComponent(){
    const [mapHtml, setMapHtml] = useState('');

    useEffect(() => {
        // Отримуємо HTML-карту з бекенду
        fetch('/ukraine_map')
          .then((response) => response.text())
          .then((html) => {
            setMapHtml(html); // Зберігаємо HTML контент
          })
          .catch((error) => console.error('Error fetching map:', error));
      }, []);
    
    return(
        <div>
            <h2>Shelling Map of Ukraine</h2>
            {mapHtml ? 
                (<div 
                    dangerouslySetInnerHTML={{ __html: mapHtml }} 
                    style={{ width: '100%', height: '600px' }} 
                />) : (<p>Loading...</p>)
                
            }
        </div>
    )

}