const staticBase = document.getElementById('component-loader').dataset.staticBase;

if (document.querySelector('form-wrapper')) {
	import(staticBase + 'components/FormWrapper.js');
}