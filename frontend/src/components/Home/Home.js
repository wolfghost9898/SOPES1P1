import React,{Component} from 'react';
import Oraciones from './Oracion/Oracion'
class Home extends Component{
    
    
    state = {
        oraciones: [],
        url : 'http://192.168.1.32/getAll'
    }
    componentDidMount(){
        document.title = "Home"

        fetch(this.state.url)
        .then(response => response.json())
        .then(data =>{
            data = data['result']
            this.setState({oraciones : data})
            console.log(data)
        })
        .catch(console.log);
    }

    render(){
        return(
            <main role="main" className="flex-shrink-0 mt-5">
                <div className="container-full">
                    <Oraciones oraciones = {this.state.oraciones}/>
                </div>
            </main>
        );
    }
}


export default Home;