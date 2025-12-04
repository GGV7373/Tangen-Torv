// --- Dark mode toggle (static button) ---
function setDarkMode(on) {
	document.documentElement.classList.toggle('dark', on);
	localStorage.setItem('darkMode', on ? '1' : '0');
	const icon = document.getElementById('darkmode-icon');
	if (icon) icon.textContent = on ? '☀️' : '🌙';
}

function getDarkModePref() {
	const stored = localStorage.getItem('darkMode');
	if (stored !== null) return stored === '1';
	return window.matchMedia('(prefers-color-scheme: dark)').matches;
}

document.addEventListener('DOMContentLoaded', function() {
	// Set initial dark mode
	setDarkMode(getDarkModePref());
	// Setup toggle button
	const btn = document.getElementById('darkmode-toggle');
	if (btn) {
		btn.addEventListener('click', function() {
			const isDark = !document.documentElement.classList.contains('dark');
			setDarkMode(isDark);
		});
	}
});

// Page fade-in effect
document.addEventListener('DOMContentLoaded', () => {
	document.body.style.opacity = 0;
	document.body.style.transition = 'opacity 0.8s cubic-bezier(.4,0,.2,1)';
	setTimeout(() => { document.body.style.opacity = 1; }, 60);
});

// Ripple effect for all .btn
document.addEventListener('click', function(e) {
	const btn = e.target.closest('.btn');
	if (!btn) return;
	let ripple = document.createElement('span');
	ripple.className = 'ripple';
	const rect = btn.getBoundingClientRect();
	ripple.style.left = (e.clientX - rect.left) + 'px';
	ripple.style.top = (e.clientY - rect.top) + 'px';
	btn.appendChild(ripple);
	setTimeout(() => ripple.remove(), 600);
});

// Add ripple CSS
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
.btn { position: relative; overflow: hidden; }
.ripple {
	position: absolute;
	border-radius: 50%;
	transform: scale(0);
	animation: ripple 0.6s linear;
	background: rgba(122,45,43,0.18);
	pointer-events: none;
	width: 120px; height: 120px;
	left: 50%; top: 50%;
	margin-left: -60px; margin-top: -60px;
	z-index: 2;
}
@keyframes ripple {
	to { transform: scale(2.5); opacity: 0; }
}
`;
document.head.appendChild(rippleStyle);

// Scroll-to-top button
const scrollBtn = document.createElement('button');
scrollBtn.textContent = '↑';
scrollBtn.setAttribute('aria-label', 'Til toppen');
scrollBtn.style.position = 'fixed';
scrollBtn.style.bottom = '2.2rem';
scrollBtn.style.right = '1.5rem';
scrollBtn.style.background = 'var(--accent)';
scrollBtn.style.color = '#fff';
scrollBtn.style.border = 'none';
scrollBtn.style.borderRadius = '50%';
scrollBtn.style.width = '2.6rem';
scrollBtn.style.height = '2.6rem';
scrollBtn.style.fontSize = '1.3rem';
scrollBtn.style.boxShadow = '0 4px 16px rgba(0,0,0,0.10)';
scrollBtn.style.cursor = 'pointer';
scrollBtn.style.opacity = '0';
scrollBtn.style.pointerEvents = 'none';
scrollBtn.style.transition = 'opacity 0.3s';
scrollBtn.style.zIndex = '100';
document.body.appendChild(scrollBtn);

window.addEventListener('scroll', () => {
	if (window.scrollY > 200) {
		scrollBtn.style.opacity = '1';
		scrollBtn.style.pointerEvents = 'auto';
	} else {
		scrollBtn.style.opacity = '0';
		scrollBtn.style.pointerEvents = 'none';
	}
});
scrollBtn.addEventListener('click', () => {
	window.scrollTo({ top: 0, behavior: 'smooth' });
});