import React, { useState, useEffect } from 'react';

export default function MapComponent(){
    const [mapHtml, setMapHtml] = useState('');

    useEffect(() => {
        fetch('/ukraine_map')
          .then((response) => response.blob())
          .then((blob) => {
            const url = URL.createObjectURL(blob);
            setMapHtml(url);
          })
          .catch((error) => console.error('Error fetching map:', error));
      }, []);
    
    return(
        <div>
            <div className='label-container'>
                <h1 className='mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-button md:text-5xl lg:text-4xl dark:text-white'>Shelling Map of Ukraine</h1>
            </div>
            {mapHtml ? 
            (<iframe 
                src={mapHtml} 
                style={{ width: '80%', height: '600px', margin: '2% 5% 2% 10%'}}
                title="Shelling Map"
            />)
                 : (<p>Loading...</p>)
            }
        </div>
    )
}