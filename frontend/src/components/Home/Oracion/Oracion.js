import React from 'react'

const Oraciones = ({oraciones}) =>{
 
    return(
        <div>      
          {oraciones.map((oracion,i) => (
            <div className="card border-info mt-2 mb-2 bg-dark text-white" key={i}>
              <h5 className="card-header">{oracion.usuario}</h5>
              <div className="card-body">
                <p className="card-text">{oracion.oracion}</p>
              </div>
            </div>
          ))}
        </div>
    );
}

export default Oraciones