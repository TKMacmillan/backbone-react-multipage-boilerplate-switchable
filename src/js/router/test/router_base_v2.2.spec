describe('suite of tests for the router base js', function() {
  it('should not be changed', function() {
    console.log('The router base js should not be changed.');
    var checksum = objectHash(routerSetupConfig);
    expect(checksum).toBe('0436d9c66802e19ec0a56bb0a902c4f604e55543');
  });
});