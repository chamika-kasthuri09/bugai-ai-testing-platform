// Fixed fixture smoke check. This does not accept or execute generated test cases.
import { chromium } from "playwright";

const browser = await chromium.launch({ chromiumSandbox: true });
try {
  const context = await browser.newContext({
    acceptDownloads: false,
    serviceWorkers: "block",
    locale: "en-US",
    timezoneId: "UTC",
    viewport: { width: 1280, height: 720 },
  });
  context.setDefaultTimeout(5000);
  context.setDefaultNavigationTimeout(10000);
  await context.route("**/*", async (route) => {
    if (new URL(route.request().url()).origin === "http://127.0.0.1:8080") {
      await route.continue();
    } else {
      await route.abort("blockedbyclient");
    }
  });
  const page = await context.newPage();
  await page.goto("http://127.0.0.1:8080");
  await page.getByRole("button", { name: "Submit" }).click();
  const message = await page.getByRole("status").textContent();
  if (message !== "Email is required") {
    throw new Error(`Unexpected fixture result: ${message}`);
  }
  await page.screenshot({ path: "artifacts/smoke.png" });
  await context.close();
  console.log("Fixture browser check passed");
} finally {
  await browser.close();
}
