export default function HomePage() {
  return (
    <main
      style={{
        maxWidth: "640px",
        width: "100%",
        padding: "2rem",
        borderRadius: "1.25rem",
        border: "1px solid rgba(255,255,255,0.2)",
        background: "rgba(7, 11, 19, 0.8)",
        boxShadow: "0 20px 50px rgba(0,0,0,0.45)"
      }}
    >
      <p style={{ textTransform: "uppercase", letterSpacing: "0.2em", fontSize: "0.8rem", opacity: 0.7 }}>
        Trading Journal
      </p>
      <h1 style={{ fontSize: "2.5rem", margin: "0.5rem 0 1rem" }}>Frontend Placeholder</h1>
      <p style={{ lineHeight: 1.6 }}>
        This Next.js app will power the dashboards, watchlists, and paper-trading flows described in the PRD. Swap this
        placeholder once the shared component library and API integrations are ready.
      </p>
    </main>
  );
}
