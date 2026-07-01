import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";

export default function Home() {
  return (
    <Layout title="Strique SEO AI Docs" description="Strique SEO AI documentation">
      <main className="home-main">
        <section className="home-section">
          <h1>Strique SEO AI Docs</h1>
          <p>
            Audit harness, checklist encyclopedia, agent contracts, skill rules,
            and connector policy for the Strique SEO module.
          </p>
          <Link className="button button--primary" to="/docs/">
            Open Docs
          </Link>
        </section>
      </main>
    </Layout>
  );
}
