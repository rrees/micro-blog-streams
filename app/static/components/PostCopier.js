class PostCopier extends HTMLElement {

	constructor() {
		super();
		this.abortController = new 	AbortController();
	}

	connectedCallback() {
		const copyLinks = this.querySelector('.content-copier');

		copyLinks.classList.remove('d-none');

		// console.log(copyLinks);

		async function handleCopyClick(event) {
			const targetId = event.target.getAttribute('data-post-id');
			const targetElement = document.querySelector(`#${targetId}`);

			// console.log(`#${targetId}`);
			await navigator.clipboard.writeText(targetElement.value);
		}
		
		copyLinks.addEventListener(
			'click',
			handleCopyClick,
			{signal: this.abortController.signal}
		);
	}

	disconnectedCallback() {
		this.abortController.abort();
	}
}

customElements.define('post-copier', PostCopier);