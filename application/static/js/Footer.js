const footerTemplate = document.createElement('template');
footerTemplate.innerHTML = `
  <style>

    html, body {
      display: table;
      margin: 0;
      height: 100%;
      width: 100%
    }

    footer {
      padding: 0 10px;
      list-style: none;
      justify-content: space-between;
      align-items: center;
      background-color: #eeeeee;
      height: 60px;
      display: flex;
    }
    
    ul li {
      list-style: none;
      display: inline;
    }
    
    a {
      margin: 0 15px;
      color: inherit;
      text-decoration: none;
    }
    
    a:hover {
      padding-bottom: 5px;
      box-shadow: inset 0 -2px 0 0 #333;
    }
    
    .social-row {
      font-size: 20px;
    }
    
    .social-row li a {
      margin: 0 15px;
    }

  </style>
  <footer>
    <a class = "note" href = "https://flask.palletsprojects.com/en/2.0.x/">Powered by Flask</a>
    <ul class="social-row">
      <li><a href="https://github.com/my-github-profile"><i class="fab fa-github"></i>
      </a></li>
      <li><a href="https://twitter.com/my-twitter-profile"><i class="fab fa-twitter"></i></a></li>
      <li><a href="https://www.linkedin.com/in/my-linkedin-profile"><i class="fab fa-linkedin"></i></a></li>
    </ul>
  </footer>
`;

class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'open' });
    shadowRoot.appendChild(footerTemplate.content);
  }
}

customElements.define('footer-component', Footer);
