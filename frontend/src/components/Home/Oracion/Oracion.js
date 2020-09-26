import React from 'react'

const Oraciones = ({oraciones}) =>{
 
    return(
        <div>      
          {oraciones.map((oracion,i) => (
            <div className="card" key={i}>
              <div className="card-body">
                <h5 className="card-title">{oracion.oracion}</h5>
                <p className="card-text">{oracion.usuario}</p>
              </div>
            </div>
          ))}
        </div>
    );
}

export default Oraciones