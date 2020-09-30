import React,{Component} from 'react';
import Oraciones from './Oracion/Oracion'
import './Style.css'

class Home extends Component{
    
    index = 0;
    intervalID;
    state = {
        oraciones: [],
        url : ['http://18.221.219.89/getAll','http://18.223.23.220/getAll']
    }

    constructor(){
        super()
        this.getData = this.getData.bind(this)
        this.tipoServidor = this.tipoServidor.bind(this)
    }

    
    componentDidMount(){
        document.title = "Home"
        this.getData()
        this.intervalID = setInterval(this.getData,5000)
    }

    componentWillUnmount() {
        clearTimeout(this.intervalID);
        console.log("Dejando de escuchar")

    }


    getData(){
        fetch(this.state.url[this.index])
        .then(response => response.json())
        .then(data =>{
            data = data['result']
            this.setState({oraciones : data})
            //console.log(data)
            
        })
        .catch(err =>{
            console.error(err)
            this.setState({oraciones:[]})
        });
    }

    tipoServidor(event){
        this.index = event.target.value;
        this.getData()
        //console.log(event.target.value)
    }


    render(){
        return(
            <main role="main" className="flex-shrink-0 mt-5 main">
                <div className="container py-md-4">
                    <select  className="select mt-2" onChange={this.tipoServidor}>
                        <option  defaultValue value="0">Servidor A</option>
                        <option value="1">Servidor B</option>
                    </select>


                    <Oraciones oraciones = {this.state.oraciones}/>
                </div>
            </main>
        );
    }
}


export default Home;