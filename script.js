const projects = [
  {
    id: "ai-factuality",
    title: "AI Factuality Detection",
    subtitle: "NLP · Weighted Ensemble · Data4Good Competition",
    date: "Nov 2025 - Jan 2026",
    description:
      "Weighted soft-voting ensemble combining HistGradientBoosting and Random Forest to detect factuality of AI-generated educational content.",
    highlights: [
      "Achieved 0.9354 Macro-AUC using semantic similarity and dual-vectorization.",
      "Engineered Jaccard similarity, TF-IDF cosine similarity, and word ratio features.",
      "Built a scalable framework for factuality validation and quality assurance.",
    ],
    tags: ["NLP", "Ensemble", "Feature Engineering", "AUC 0.9354"],
    kpis: [
      { label: "Macro AUC", value: "0.9354" },
      { label: "CV Folds", value: "5" },
      { label: "Train Size", value: "21,021" },
    ],
    category: ["ml", "nlp"],
    image:
      "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=900&q=80",
    link: "https://github.com/Debadri1999/AI-Factuality-Detection-ML",
  },
  {
    id: "bankruptcy-system",
    title: "Bankruptcy Prediction System",
    subtitle: "Risk Modeling · Dual-Model Ensemble",
    date: "Oct 2025 - Dec 2025",
    description:
      "Production-ready bankruptcy risk engine using algorithm-specific feature engineering and 100-model ensemble.",
    highlights: [
      "Final system reached 0.917 public AUC and 0.909 private AUC.",
      "Applied heavy/light feature engineering to LightGBM and XGBoost paths.",
      "Implemented 5-seed × 10-fold stratified CV for robust predictions.",
    ],
    tags: ["Risk", "LightGBM", "XGBoost", "AUC 0.917"],
    kpis: [
      { label: "Public AUC", value: "0.917" },
      { label: "Private AUC", value: "0.909" },
      { label: "Models", value: "100" },
    ],
    category: ["ml"],
    image:
      "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=900&q=80",
    link: "https://github.com/Debadri1999/bankruptcy-prediction-system",
  },
  {
    id: "computer-price",
    title: "Computer Price Dynamics Analysis",
    subtitle: "EDA · Hypothesis Testing",
    date: "Aug 2025 - Oct 2025",
    description:
      "Exploratory analysis of 100k computer systems to quantify how specs influence market valuation.",
    highlights: [
      "Built tiered pricing models from hypothesis testing insights.",
      "Analyzed spec impact with Python (Pandas, NumPy) workflows.",
      "Translated analytics into product positioning strategies.",
    ],
    tags: ["EDA", "Hypothesis", "Python"],
    kpis: [
      { label: "Systems Analyzed", value: "100k+" },
      { label: "Features", value: "30+" },
      { label: "Hypotheses", value: "8" },
    ],
    category: ["analytics"],
    image:
      "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
    link: "https://github.com/Debadri1999/computer-price-analysis",
  },
  {
    id: "accrual-anomaly",
    title: "Financial Portfolio Analysis",
    subtitle: "Accrual Anomaly Portfolio · Time-Series",
    date: "2025",
    description:
      "Empirical analysis of accrual anomaly using Kenneth French data, comparing low vs high accrual deciles across market cycles.",
    highlights: [
      "Constructed 10 decile portfolios with equal- and value-weighted returns.",
      "Measured spread portfolio performance and recession vs expansion regimes.",
      "Confirmed low-accrual firms outperform high-accrual firms over 1963-2025.",
    ],
    tags: ["Portfolio", "Financial Markets", "Time-Series"],
    kpis: [
      { label: "Sample Years", value: "1963-2025" },
      { label: "Deciles", value: "10" },
      { label: "Weighting", value: "EW + VW" },
    ],
    category: ["analytics"],
    image:
      "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=900&q=80",
    link: "Accrual_Anamoly_Final_Project/Final%20Project/Accrual_Anomaly_Analysis_Report%20final.pdf",
  },
  {
    id: "doubledo-gaming-chatbot",
    title: "AI Chatbot for Gaming Industry",
    subtitle: "Gaming Hardware Expert · Chatbase AI",
    date: "Dec 2025",
    description:
      "A 24/7 gaming hardware expert assistant that delivers build recommendations, compatibility checks, and deal alerts.",
    highlights: [
      "Achieved an estimated 85%+ query resolution rate without human escalation.",
      "Translated technical specs into budget-aware recommendations.",
      "Designed FAQ coverage and quick actions for common customer needs.",
    ],
    tags: ["Conversational AI", "Chatbase", "Customer Support"],
    kpis: [
      { label: "Resolution Rate", value: "85%+" },
      { label: "Response Time", value: "<3s" },
      { label: "FAQ Coverage", value: "60+" },
    ],
    category: ["automation"],
    image:
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80",
    link: "Chatbot_Project/Doubledo_Gaming_AI_Chatbot_Report.pdf",
  },
  {
    id: "nacho-nirvana-chatbot",
    title: "Food Delivery Chatbot",
    subtitle: "Chatfuel · Automated Ordering",
    date: "Dec 2025",
    description:
      "Facebook Messenger chatbot for nacho ordering with dynamic pricing, customization, and order confirmation.",
    highlights: [
      "Built a 12-block conversational flow covering the full order journey.",
      "Implemented attribute-based pricing for size, toppings, drinks, and sides.",
      "Delivered menu navigation for classic vs loaded nacho categories.",
    ],
    tags: ["Chatbot", "Chatfuel", "Automation"],
    kpis: [
      { label: "Conversation Blocks", value: "12" },
      { label: "Dynamic Pricing", value: "Yes" },
      { label: "Order Flow", value: "End-to-End" },
    ],
    category: ["automation"],
    image:
      "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=900&q=80",
    link: "Chatbot_Project/Nacho_Nirvana_Fixed_Chatbot_Report.pdf",
  },
  {
    id: "gaming-laptop",
    title: "Web Crawling Market Analysis",
    subtitle: "Web Automation · Pricing Intelligence",
    date: "Nov 2026",
    description:
      "Web-crawled laptop listings to benchmark price-performance and track competitive market positioning.",
    highlights: [
      "Automated capture of specs, price points, and availability signals.",
      "Compared configurations to surface best-value performance tiers.",
      "Built a clean dataset for downstream pricing analytics.",
    ],
    tags: ["Web Scraping", "Market Analysis", "Automation"],
    kpis: [
      { label: "Listings Captured", value: "2k+" },
      { label: "Pricing Tiers", value: "5" },
      { label: "Refresh Cadence", value: "Weekly" },
    ],
    category: ["automation", "analytics"],
    image:
      "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=900&q=80",
    link: "Gaming_Laptop_Webscraping_Market_Analysis/",
  },
];

const page = document.body.dataset.page;

const initParticles = () => {
  const canvas = document.getElementById("bg-canvas");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const particles = [];
  const density = 70;

  const resize = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  };

  const createParticles = () => {
    particles.length = 0;
    for (let i = 0; i < density; i += 1) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 1.8 + 0.6,
        speed: Math.random() * 0.4 + 0.1,
        direction: Math.random() * Math.PI * 2,
      });
    }
  };

  const draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "rgba(106, 227, 255, 0.7)";

    particles.forEach((p) => {
      p.x += Math.cos(p.direction) * p.speed;
      p.y += Math.sin(p.direction) * p.speed;
      if (p.x < 0 || p.x > canvas.width) p.direction = Math.PI - p.direction;
      if (p.y < 0 || p.y > canvas.height) p.direction = -p.direction;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fill();
    });

    for (let i = 0; i < particles.length; i += 1) {
      for (let j = i + 1; j < particles.length; j += 1) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.strokeStyle = `rgba(106, 227, 255, ${0.12 - dist / 1200})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  };

  resize();
  createParticles();
  draw();
  window.addEventListener("resize", () => {
    resize();
    createParticles();
  });
};

const initReveal = () => {
  const reveals = document.querySelectorAll(".reveal");
  if (!reveals.length) return;
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    { threshold: 0.3 }
  );
  reveals.forEach((el) => observer.observe(el));
};

const animateCounters = () => {
  const counters = document.querySelectorAll("[data-count]");
  counters.forEach((counter) => {
    const target = Number(counter.dataset.count || 0);
    let current = 0;
    const step = Math.max(1, Math.round(target / 60));
    const tick = () => {
      current = Math.min(target, current + step);
      counter.textContent = `${current}${target > 10 ? "%" : "+"}`;
      if (current < target) requestAnimationFrame(tick);
    };
    tick();
  });
};


const renderProjectsPage = () => {
  const grid = document.getElementById("projects-grid");
  if (!grid) return;

  const renderCards = (filter) => {
    grid.innerHTML = "";
    const filtered = projects.filter((project) =>
      filter === "all" ? true : project.category.includes(filter)
    );
    filtered.forEach((project) => {
      const card = document.createElement("article");
      card.className = "card project-card glass reveal";
      card.innerHTML = `
        <img class="project-image" src="${project.image}" alt="${project.title}" loading="lazy" />
        <div class="project-header">
          <h3>${project.title}</h3>
          <span class="tag">${project.date}</span>
        </div>
        <p>${project.description}</p>
        <div class="kpi-row">
          ${project.kpis
            .map((kpi) => `<div class="kpi-chip"><span>${kpi.value}</span>${kpi.label}</div>`)
            .join("")}
        </div>
        <div class="tag-row">
          ${project.tags.map((tag) => `<span>${tag}</span>`).join("")}
        </div>
        <button class="btn btn-ghost" data-project="${project.id}">View Details</button>
      `;
      grid.appendChild(card);
    });
    initReveal();
  };

  const modal = document.getElementById("project-modal");
  const modalTitle = document.getElementById("modal-title");
  const modalSubtitle = document.getElementById("modal-subtitle");
  const modalDescription = document.getElementById("modal-description");
  const modalHighlights = document.getElementById("modal-highlights");
  const modalTags = document.getElementById("modal-tags");
  const modalImage = document.getElementById("modal-image");
  const modalLink = document.getElementById("modal-link");
  const modalKpis = document.getElementById("modal-kpis");

  const openModal = (project) => {
    modalTitle.textContent = project.title;
    modalSubtitle.textContent = project.subtitle;
    modalDescription.textContent = project.description;
    modalHighlights.innerHTML = project.highlights
      .map((item) => `<li>${item}</li>`)
      .join("");
    modalTags.innerHTML = project.tags.map((tag) => `<span>${tag}</span>`).join("");
    modalImage.src = project.image;
    modalImage.alt = project.title;
    modalLink.href = project.link;
    modalKpis.innerHTML = project.kpis
      .map((kpi) => `<div class="kpi-chip"><span>${kpi.value}</span>${kpi.label}</div>`)
      .join("");
    modal.classList.add("show");
    modal.setAttribute("aria-hidden", "false");
  };

  const closeModal = () => {
    modal.classList.remove("show");
    modal.setAttribute("aria-hidden", "true");
  };

  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-project]");
    if (trigger) {
      const project = projects.find((p) => p.id === trigger.dataset.project);
      if (project) openModal(project);
    }
    if (event.target.matches("[data-close]")) {
      closeModal();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeModal();
  });

  const filterButtons = document.querySelectorAll(".filter-btn");
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderCards(btn.dataset.filter);
    });
  });

  renderCards("all");
};

const initSpotlight = () => {
  const titleEl = document.getElementById("spotlight-title");
  const tagEl = document.getElementById("spotlight-tag");
  if (!titleEl || !tagEl) return;
  let index = 0;
  const rotate = () => {
    const project = projects[index % projects.length];
    titleEl.textContent = project.title;
    tagEl.textContent = project.tags[0];
    index += 1;
  };
  rotate();
  setInterval(rotate, 4000);
};

initParticles();
initReveal();
animateCounters();
initSpotlight();

if (page === "projects") {
  renderProjectsPage();
}
