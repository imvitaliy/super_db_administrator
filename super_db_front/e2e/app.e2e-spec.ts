import { SuperDbFrontPage } from './app.po';

describe('super-db-front App', function() {
  let page: SuperDbFrontPage;

  beforeEach(() => {
    page = new SuperDbFrontPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
