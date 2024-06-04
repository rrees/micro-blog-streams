
console.log('Hello world');

class TopicFilter extends HTMLElement {
	constructor() {
		super();
	}

	connectedCallback() {
		const component = this;

		const wrapper = document.querySelector('#topic-filter-wrapper');
		const filter = document.querySelector('#topic-filter');

		wrapper.removeAttribute('hidden');
	}
}

customElements.define('topic-filter', TopicFilter);