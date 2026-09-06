class FormWrapper extends HTMLElement {
	connectedCallback() {
		console.log('FormWrapper connected');
	}
}

customElements.define('form-wrapper', FormWrapper);