class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>
        .header {
            background-color: #88BACF;
            height: 73px;
            line-height: 70px;
            position: fixed;
            top: 0;
            width:100%;
            z-index: 999;
        }
        

        .logo img{
            
            float: left;
            
            background-repeat: no-repeat;
            background-size: cover;
            padding: 5px 0px 5px 0px;
            margin: 0px;
            width: 130px;
            height: 70px;
        }
        
       

        .menu {
            float: right;
        }
        
        .menu a {
            color: #ffffff;
            margin-right: 20px;
        }
        
        .menu a:hover {
            color: #547280;
        }
        
        .container-fluid {
            padding: 0;
        }

          

        </style>
        <header class="container-fluid header" id="myHeader">
            <div class="container">
                <a href='/' class="logo"><img src="/static/img/logo_tn.png" alt="logo"/></a>
                <nav class="menu">
                    <a href='/charts'>Statistiques</a>
                    <a href='/parcours'>Parcours des données</a>
                    <a href='/recherches'>Recherches</a>
                </nav>
            </div>
        </header>
      `;

    }
}

customElements.define('header-component', Header);
  
