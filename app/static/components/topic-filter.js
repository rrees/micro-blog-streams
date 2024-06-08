
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

		filter.addEventListener('input', (event) => {
			console.log('Filter change', event.target.value);
			const filterRegularExpression = new RegExp(event.target.value, "i");

			const topics = document.querySelectorAll('.topic');
			const topicLinks = document.querySelectorAll('.topic-link');

			for(const topic of topics) {
				topic.removeAttribute('hidden');
			}

			for(const link of topicLinks) {
				if(!filterRegularExpression.test(link.text)) {
					link.parentElement.setAttribute('hidden', 'hidden');
				}
			}
		})
	}
}

customElements.define('topic-filter', TopicFilter);