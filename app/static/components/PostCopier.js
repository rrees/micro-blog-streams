class PostCopier extends HTMLElement {

	constructor() {
		super();
		this.abortController = new 	AbortController();
	}

	connectedCallback() {
		const messageDisplayDuration = 1.5 * 1000;

		const copyLinks = this.querySelector('.content-copier');

		copyLinks.classList.remove('d-none');

		// console.log(copyLinks);

		async function handleCopyClick(event) {
			const eventTarget = event.target;
			const targetId = eventTarget.getAttribute('data-post-id');
			const targetElement = document.querySelector(`#${targetId}`);

			// console.log(`#${targetId}`);
			await navigator.clipboard.writeText(targetElement.value);

			const initialContent = eventTarget.innerText;

			eventTarget.innerText = "Content copied!";

			setTimeout(() => {eventTarget.innerText = initialContent;}, messageDisplayDuration);

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