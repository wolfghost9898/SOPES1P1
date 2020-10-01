import React,{Component} from 'react';

class Home extends Component{
    componentDidMount(){
        document.title = "Error 404"
    }

    render(){
        return(
            <main role="main" className="flex-shrink-0 mt-5">
                <br></br>
               <h1>Pagina no Encontrada :(</h1>
            </main>
        );
    }
}


export default Home;