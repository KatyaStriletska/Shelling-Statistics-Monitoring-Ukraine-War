import React, { useState, useEffect } from 'react';

export default function MapComponent(){
    const [mapHtml, setMapHtml] = useState('');

    useEffect(() => {
        // Отримуємо HTML-карту з бекенду
        fetch('/ukraine_map')
          .then((response) => response.blob())
          .then((blob) => {
            // console.log(html); // Дивимось, що приходить

            // setMapHtml(html); // Зберігаємо HTML контент
            const url = URL.createObjectURL(blob);
            setMapHtml(url);
          })
          .catch((error) => console.error('Error fetching map:', error));
      }, []);
    
    return(
        <div>
            <div>
            <h1>Shelling Map of Ukraine</h1>
            </div>
            {mapHtml ? 
            (<iframe 
                src={mapHtml} 
                style={{ width: '80%', height: '600px', margin: '2% 5% 2% 10%'}}
                title="Shelling Map"
            />)
                // (<div 
                //     dangerouslySetInnerHTML={{ __html: mapHtml }} 
                //     style={{ width: '100%', height: '600px' }} 
                // />)
                 : (<p>Loading...</p>)
            }
        </div>
    )
// border: '2px solid
}