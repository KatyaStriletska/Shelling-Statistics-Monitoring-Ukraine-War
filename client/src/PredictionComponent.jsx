import React, { useState, useEffect } from 'react';

export default function PredictionComponent({apiUrl}){
    const fetchPred = (year, place, launched) =>{
        fetch(`${apiUrl}?year=${year}&place=${place}&launched=${launched}`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data)
            })
            .catch((err) => console.log("Error fetching categories:", err));
    }
    useEffect(() => {
        fetchPred(2022, "Black Sea", 4)
    }, []);
    
    return(
        <div>
        
        </div>
    )
}