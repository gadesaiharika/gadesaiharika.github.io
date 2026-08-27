/* Portfolio behaviour: theme, nav, scroll-spy, reveal.
   No dependencies. Everything degrades to a working page if JS never runs. */
(function () {
  "use strict";

  /* ---- theme ----------------------------------------------------------
     The inline script in <head> has already applied the stored theme, so
     there is no flash. This only wires the toggle. */
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");

  function currentTheme() {
    var stamped = root.getAttribute("data-theme");
    if (stamped) return stamped;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      toggle.setAttribute("aria-label", "Switch to " + (next === "dark" ? "light" : "dark") + " theme");
      try { localStorage.setItem("theme", next); } catch (e) { /* private mode */ }
    });
  }

  /* ---- sticky nav shadow ---------------------------------------------- */
  var nav = document.querySelector(".nav");
  if (nav) {
    var onScroll = function () {
      nav.setAttribute("data-scrolled", window.scrollY > 8 ? "true" : "false");
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- mobile menu ----------------------------------------------------- */
  var navToggle = document.querySelector("[data-nav-toggle]");
  var navLinks = document.getElementById("nav-links");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      var open = navLinks.getAttribute("data-open") === "true";
      navLinks.setAttribute("data-open", open ? "false" : "true");
      navToggle.setAttribute("aria-expanded", open ? "false" : "true");
    });
    navLinks.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        navLinks.setAttribute("data-open", "false");
        navToggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---- reveal on scroll ------------------------------------------------ */
  var revealables = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    // No observer or the visitor asked for less motion: show everything now.
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    Array.prototype.forEach.call(revealables, function (el, i) {
      // Stagger siblings slightly so a grid resolves in sequence, not all at once.
      el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + "ms";
      io.observe(el);
    });
  }

  /* ---- scroll spy ------------------------------------------------------ */
  var spyLinks = Array.prototype.slice.call(
    document.querySelectorAll('.nav__links a[href^="#"]'));
  if (spyLinks.length && "IntersectionObserver" in window) {
    var sections = spyLinks
      .map(function (a) { return document.querySelector(a.getAttribute("href")); })
      .filter(Boolean);

    var setCurrent = function (id) {
      spyLinks.forEach(function (a) {
        a.setAttribute("aria-current",
          a.getAttribute("href") === "#" + id ? "true" : "false");
      });
    };

    var spy = new IntersectionObserver(function (entries) {
      // Pick the entry nearest the top of the viewport that is on screen,
      // so fast scrolling never leaves two links lit or none.
      var visible = entries.filter(function (e) { return e.isIntersecting; });
      if (!visible.length) return;
      visible.sort(function (a, b) {
        return a.boundingClientRect.top - b.boundingClientRect.top;
      });
      setCurrent(visible[0].target.id);
    }, { rootMargin: "-66px 0px -62% 0px", threshold: 0 });

    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---- year ------------------------------------------------------------ */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
})();
