class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>
        .header {
            background-color: #88BACF;
            height: 70px;
            line-height: 70px;
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
                <a href='index' class="logo"><img src="static/img/logo_tn.png" alt="logo"/></a>
                <nav class="menu">
                    <a href='#'> Accueil</a>
                    <a href='#about'>TIPE</a>
                    <a href='#ecole'> Ecoles</a>
                    <a href='#Contact'> Contact</a>
                </nav>
            </div>
        </header>
      `;

    }
}

customElements.define('header-component', Header);
  