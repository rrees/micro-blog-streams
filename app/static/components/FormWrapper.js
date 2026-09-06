class FormWrapper extends HTMLElement {
	constructor() {
		super();

		this.form = this.querySelector('form');

		this.form.addEventListener('submit', this);

		this.statusAttributeName = 'form-submitting';

		this.delay = 500;
		this.debug = true;
	}

	disable() {
		this.setAttribute(this.statusAttributeName, '');
	}

	enable() {
		this.removeAttribute(this.statusAttributeName);
	}

	isDisabled() {
		return this.hasAttribute(this.statusAttributeName);
	}


	handleEvent(event) {
		//console.log(event);
		this[`on${event.type}`](event);
	}

	async onsubmit(event) {
		event.preventDefault();

		//console.log('Form submitting');

		if(this.isDisabled()) {
			//console.log('Form disabled')
			return;
		}

		this.disable();

		try {
			const {action, method} = this.form;

			if(this.debug) {
				console.log(action, method);
			}

			const response = await fetch(action, {
				method: method,
				body: new FormData(this.form)
			});

			const data = response;

			window.location.href = data.url;

		} catch(error) {
			console.log(error);
			
			setTimeout(() => this.enable(), this.delay);
		}
	}

	connectedCallback() {
		console.log('FormWrapper connected');
	}
}

customElements.define('form-wrapper', FormWrapper);